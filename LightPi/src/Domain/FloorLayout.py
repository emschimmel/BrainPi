import sys
sys.path.append('../src/gen-py')
from LightPi.ttypes import GetFloorOutput
from LightPi.ttypes import Floor
from LightPi.ttypes import Room
from LightPi.ttypes import Device
import json


class FloorLayout:

    floor_collection = []

    def __init__(self):
        self.floor_collection = self.__JsonToThrift(self.__load_layout_file())

    def getLayout(self):
        return self.floor_collection

    def storeLayout(self, input):
        with open('./Memory/personMock.json', 'w') as outfile:
            json.dump(input, outfile)
        self.floor_collection = self.__JsonToThrift(self.__load_layout_file())

    @staticmethod
    def __JsonToThrift(jsondata):
        thrift = GetFloorOutput()
        thrift.floorCollection = []
        JsonfloorCollection = jsondata['floorCollection']
        for floor in JsonfloorCollection:
            thriftFloor = Floor()
            thriftFloor.number = floor['number']
            thriftFloor.name = floor['name']
            thriftFloor.enabled = floor['enabled']
            thriftFloor.roomCollection = []
            JsonRoomCollection = floor['roomCollection']
            for room in JsonRoomCollection:
                thriftRoom = Room()
                thriftRoom.number = room['number']
                thriftRoom.name = room['name']
                thriftRoom.enabled = room['enabled']
                thriftRoom.deviceCollection = []
                JsonDeviceCollection = floor['deviceCollection']
                for device in JsonDeviceCollection:
                    thriftDevice = Device()
                    thriftDevice.number = device['number']
                    thriftDevice.name = device['name']
                    thriftDevice.enabled = device['enabled']
                    thriftDevice.type = device['type']
                    thriftRoom.deviceCollection.append(thriftDevice)
                thriftFloor.roomCollection.append(thriftRoom)
            thrift.floorCollection.append(thriftFloor)
        return thrift

    @staticmethod
    def __load_layout_file():
        return json.load(open('./Memory/personMock.json'))