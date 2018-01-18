#https://github.com/picklepete/pyicloud

from datetime import datetime
from pyicloud import PyiCloudService
import sys
sys.path.append('../gen-py')
from ThriftException.ttypes import ExternalEndpointUnavailable

class PhotoConnect:

    @staticmethod
    def getMultiple(input):
        try:
            api = PyiCloudService(input.email)
            photos = []
            for _, photo in zip(range(input.limit), api.photos.all):
                photos.append(photo)
            return photos
        except Exception as ex:
            print(ex)
            raise ExternalEndpointUnavailable("PhotoPi", "Device needs to be registered", "icloud")

    @staticmethod
    def getRandom(input):
        try:
            api = PyiCloudService(input.email)
            photo = next(iter(api.photos.all), None)
            download = photo.download()
            return download.raw.read()
        except Exception as ex:
            print(ex)
            raise ExternalEndpointUnavailable("PhotoPi", "Device needs to be registered", "icloud")
