from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.append('./gen-py')

from FacePi.ttypes import PersonEntry

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow.python.platform import gfile
import numpy as np
import sys
from .DetectAndAlign import DetectAndAlign as detect_and_align
from .IdData import getIdData as id_data
from scipy import misc
import re
import cv2
import time
import pickle
sys.path.append('../../')
import config

class StartTensor():

    def __init__(self):
        pass

    @classmethod
    def find_matching_id(self, id_dataset, embedding):
        threshold = 1.1
        min_dist = 10.0
        matching_id = None

        for id_data_in_for in id_dataset:
            dist = self.get_embedding_distance(id_data_in_for.embedding, embedding)

            if dist < threshold and dist < min_dist:
                min_dist = dist
                matching_id = id_data_in_for.name
        return matching_id, min_dist

    @staticmethod
    def get_embedding_distance(emb1, emb2):
        dist = np.sqrt(np.sum(np.square(np.subtract(emb1, emb2))))
        return dist

    @classmethod
    def save_model(self):
        model_exp = config.tensor_model_path
        meta_file, ckpt_file = self.get_model_filenames()
        saver = tf.train.import_meta_graph(os.path.join(model_exp, meta_file))
        saver.save(self.sess, os.path.join(model_exp, ckpt_file))

    @staticmethod
    def get_model_filenames():
        model_dir = config.tensor_model_path
        files = os.listdir(model_dir)
        meta_files = [s for s in files if s.endswith('.meta')]
        if len(meta_files) == 0:
            raise ValueError('No meta file found in the model directory (%s)' % model_dir)
        elif len(meta_files) > 1:
            raise ValueError('There should not be more than one meta file in the model directory (%s)' % model_dir)
        meta_file = meta_files[0]
        meta_files = [s for s in files if '.ckpt' in s]
        max_step = -1
        for f in files:
            step_str = re.match(r'(^model-[\w\- ]+.ckpt-(\d+))', f)
            if step_str is not None and len(step_str.groups()) >= 2:
                step = int(step_str.groups()[1])
                if step > max_step:
                    max_step = step
                    ckpt_file = step_str.groups()[0]
        return meta_file, ckpt_file

    @staticmethod
    def save_id_dataset(obj):
        with open(config.tensor_id_file, 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_id_dataset():
        try:
            with open(config.tensor_id_file, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            raise Exception

    @classmethod
    def train(self, sess):
        self.sess = sess
        try:
            from subprocess import call
            call("find ./ids/ -name '.DS_Store' -type f -delete")
        except:
            pass
        pnet, rnet, onet = detect_and_align.create_mtcnn(self.sess, None)

        # self.load_model()
        # id_dataset = self.load_id_dataset()
        images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
        embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
        phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
        id_dataset = id_data().get_id_data(config.tensor_id_file, pnet, rnet, onet, sess, embeddings, images_placeholder, phase_train_placeholder)

        self.save_model()
        self.save_id_dataset(id_dataset)
        return id_dataset

    @classmethod
    def loadWithoutTrainFromFrame(self, sess, frame):
        self.sess = sess
        personList = []
        print("in tensor 158")
        pnet, rnet, onet = detect_and_align.create_mtcnn(self.sess, None)
        # self.load_model()
        try:
            id_dataset = self.load_id_dataset()
        except:
            id_dataset = self.train(sess)
        images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
        embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
        phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
        face_patches, padded_bounding_boxes, landmarks = detect_and_align.align_image(frame, pnet, rnet, onet)
        print(face_patches)
        if len(face_patches) > 0:
            face_patches = np.stack(face_patches)
            feed_dict = {images_placeholder: face_patches, phase_train_placeholder: False}
            embs = self.sess.run(embeddings, feed_dict=feed_dict)

            print('Matches in frame:')
            for i in range(len(embs)):
                bb = padded_bounding_boxes[i]

                matching_id, dist = self.find_matching_id(id_dataset, embs[i, :])
                if matching_id:
                    person = PersonEntry()
                    person.person = matching_id
                    person.chance = dist
                    person.image = pickle.dumps(obj=frame, protocol=None, fix_imports=False)
                    person.algoritm = 'TensorFlow'
                    personList.append(person)
                    print('Hi %s! Distance: %1.4f' % (matching_id, dist))
                else:
                    matching_id = 'Unkown'
                    print('Unkown! Couldn\'t find match.')
        return personList

if __name__ == '__main__':
    try:
        from subprocess import call
        call("find ./ids/ -name '.DS_Store' -type f -delete")
    except:
        pass
