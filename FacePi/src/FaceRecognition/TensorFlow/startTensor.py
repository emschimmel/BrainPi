from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.append('./gen-py')

from FacePi import FacePiThriftService
from FacePi.ttypes import FacePiOutput
from FacePi.ttypes import PersonEntry

import tensorflow as tf
from tensorflow.python.platform import gfile
import numpy as np
import sys
import os
from .DetectAndAlign import DetectAndAlign as detect_and_align
from .IdData import IdData as id_data
from scipy import misc
import re
import cv2
import argparse
import time
import pickle
sys.path.append('../../')
import config

class StartTensor():

    @classmethod
    def find_matching_id(self, id_dataset, embedding):
        threshold = 1.1
        min_dist = 10.0
        matching_id = None

        for id_data in id_dataset:
            dist = self.get_embedding_distance(id_data.embedding, embedding)

            if dist < threshold and dist < min_dist:
                min_dist = dist
                matching_id = id_data.name
        return matching_id, min_dist

    @staticmethod
    def get_embedding_distance(emb1, emb2):
        dist = np.sqrt(np.sum(np.square(np.subtract(emb1, emb2))))
        return dist

    @classmethod
    def load_model(self, model):
        model_exp = os.path.expanduser(model)
        if (os.path.isfile(model_exp)):
            print('Model filename: %s' % model_exp)
            with gfile.FastGFile(model_exp, 'rb') as f:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())
                tf.import_graph_def(graph_def, name='')
        else:
            print('Model directory: %s' % model_exp)
            meta_file, ckpt_file = self.get_model_filenames(model_exp)

            print('Metagraph file: %s' % meta_file)
            print('Checkpoint file: %s' % ckpt_file)

            saver = tf.train.import_meta_graph(os.path.join(model_exp, meta_file))
            saver.restore(tf.get_default_session(), os.path.join(model_exp, ckpt_file))

    @classmethod
    def save_model(self, sess, model_exp):
        meta_file, ckpt_file = self.get_model_filenames(model_exp)
        saver = tf.train.import_meta_graph(os.path.join(model_exp, meta_file))
        saver.save(sess, os.path.join(model_exp, ckpt_file))

    @staticmethod
    def get_model_filenames(model_dir):
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


    @classmethod
    def print_id_dataset_table(self, id_dataset):
        nrof_samples = len(id_dataset)

        print('Images:')
        for i in range(nrof_samples):
            print('%1d: %s' % (i, id_dataset[i].image_path))
        print('')

        print('Distance matrix')
        print('         ', end='')
        for i in range(nrof_samples):
            name = os.path.splitext(os.path.basename(id_dataset[i].name))[0]
            print('     %s   ' % name, end='')
        print('')
        for i in range(nrof_samples):
            name = os.path.splitext(os.path.basename(id_dataset[i].name))[0]
            print('%s       ' % name, end='')
            for j in range(nrof_samples):
                dist = self.get_embedding_distance(id_dataset[i].embedding, id_dataset[j].embedding)
                print('  %1.4f      ' % dist, end='')
            print('')


    @classmethod
    def test_run(self, pnet, rnet, onet, sess, images_placeholder, phase_train_placeholder, embeddings, id_dataset, test_folder):
        if test_folder is None:
            return

        image_names = os.listdir(os.path.expanduser(test_folder))
        image_paths = [os.path.join(test_folder, img) for img in image_names]
        nrof_images = len(image_names)
        aligned_images = []
        aligned_image_paths = []

        for i in range(nrof_images):
            image = misc.imread(image_paths[i])
            face_patches, _, _ = detect_and_align.align_image(image, pnet, rnet, onet)
            aligned_images = aligned_images + face_patches
            aligned_image_paths = aligned_image_paths + [image_paths[i]] * len(face_patches)

        aligned_images = np.stack(aligned_images)

        feed_dict = {images_placeholder: aligned_images, phase_train_placeholder: False}
        embs = sess.run(embeddings, feed_dict=feed_dict)

        for i in range(len(embs)):
            misc.imsave('outfile' + str(i) + '.jpg', aligned_images[i])
            matching_id, dist = self.find_matching_id(id_dataset, embs[i, :])
            if matching_id:
                print('Found match %s for %s! Distance: %1.4f' % (matching_id, aligned_image_paths[i], dist))
            else:
                print('Couldn\'t find match for %s' % (aligned_image_paths[i]))

    @staticmethod
    def save_id_dataset(obj):
        with open(config.tensor_id_file, 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_id_dataset():
        with open(config.tensor_id_file, 'rb') as f:
            return pickle.load(f)

    @classmethod
    def train(self):
        from subprocess import call
        call("find ./ids/ -name '.DS_Store' -type f -delete")
        with tf.Graph().as_default():
            with tf.Session() as sess:
                pnet, rnet, onet = detect_and_align.create_mtcnn(sess, None)
                #
                self.load_model(config.tensor_model_path)
                id_dataset = self.load_id_dataset()
                images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
                embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
                phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

                self.print_id_dataset_table(id_dataset)

                self.save_model(sess, config.tensor_model_path)
                self.save_id_dataset(id_dataset)

    # self.test_run(pnet, rnet, onet, sess, images_placeholder, phase_train_placeholder, embeddings, id_dataset, args.test_folder)

    @classmethod
    def loadWithoutTrainFromFrame(self, frame):
        personList = []
        with tf.Graph().as_default():
            with tf.Session() as sess:
                pnet, rnet, onet = detect_and_align.create_mtcnn(sess, None)
                self.load_model(config.tensor_model_path)
                id_dataset = self.load_id_dataset()
                images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
                embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
                phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
                face_patches, padded_bounding_boxes, landmarks = detect_and_align.align_image(frame, pnet, rnet, onet)

                if len(face_patches) > 0:
                    face_patches = np.stack(face_patches)
                    feed_dict = {images_placeholder: face_patches, phase_train_placeholder: False}
                    embs = sess.run(embeddings, feed_dict=feed_dict)

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

    @classmethod
    def main(self):
        with tf.Graph().as_default():
            with tf.Session() as sess:

                pnet, rnet, onet = detect_and_align.create_mtcnn(sess, None)
                self.load_model(config.tensor_model_path)
                id_dataset = self.load_id_dataset()
                images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
                embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
                phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

                cap = cv2.VideoCapture(0)
                frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

                show_landmarks = False
                show_bb = False
                show_id = True
                show_fps = False
                while(True):
                    start = time.time()
                    _, frame = cap.read()

                    face_patches, padded_bounding_boxes, landmarks = detect_and_align.align_image(frame, pnet, rnet, onet)

                    if len(face_patches) > 0:
                        face_patches = np.stack(face_patches)
                        feed_dict = {images_placeholder: face_patches, phase_train_placeholder: False}
                        embs = sess.run(embeddings, feed_dict=feed_dict)

                        print('Matches in frame:')
                        for i in range(len(embs)):
                            bb = padded_bounding_boxes[i]

                            matching_id, dist = self.find_matching_id(id_dataset, embs[i, :])
                            if matching_id:
                                print('Hi %s! Distance: %1.4f' % (matching_id, dist))
                            else:
                                matching_id = 'Unkown'
                                print('Unkown! Couldn\'t find match.')

                            if show_id:
                                font = cv2.FONT_HERSHEY_SIMPLEX
                                cv2.putText(frame, matching_id, (bb[0], bb[3]), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

                            if show_bb:
                                cv2.rectangle(frame, (bb[0], bb[1]), (bb[2], bb[3]), (255, 0, 0), 2)

                            if show_landmarks:
                                for j in range(5):
                                    size = 1
                                    top_left = (int(landmarks[i, j]) - size, int(landmarks[i, j + 5]) - size)
                                    bottom_right = (int(landmarks[i, j]) + size, int(landmarks[i, j + 5]) + size)
                                    cv2.rectangle(frame, top_left, bottom_right, (255, 0, 255), 2)
                    else:
                        print('Couldn\'t find a face')

                    end = time.time()

                    seconds = end - start
                    fps = round(1 / seconds, 2)

                    if show_fps:
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(frame, str(fps), (0, int(frame_height) - 5), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

                    cv2.imshow('frame', frame)

                    key = cv2.waitKey(1)
                    if key == ord('q'):
                        break
                    elif key == ord('l'):
                        show_landmarks = not show_landmarks
                    elif key == ord('b'):
                        show_bb = not show_bb
                    elif key == ord('i'):
                        show_id = not show_id
                    elif key == ord('f'):
                        show_fps = not show_fps

                cap.release()
                cv2.destroyAllWindows()


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('model', type=str, help='Could be either a directory containing the meta_file and ckpt_file or a model protobuf (.pb) file')
    parser.add_argument('id_folder', type=str, nargs='+', help='Folder containing ID folders')
    parser.add_argument('--test_folder', type=str, help='Folder containing test images.', default=None)
    return parser.parse_args(argv)

if __name__ == '__main__':
    try:
        from subprocess import call
        call("find ./ids/ -name '.DS_Store' -type f -delete")
    except:
        pass
    # main.main(parse_arguments(sys.argv[1:]))
    main.main()
