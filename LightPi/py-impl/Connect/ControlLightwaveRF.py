from pylightwaverf import LightWaveRF as pylightwaverf
import sys
sys.path.append('../gen-py')
from LightPi.ttypes import DeviceState
from LightPi.ttypes import DeviceType

class ControlLightwaveRF:

    def handleInput(self, input):
        device = input.deviceNumber
        room = input.roomNumber
        if input.optionalValue:
            command = self.__createComand(input.optionalValue)
        else:
            command = input.state
        self.__send_command(room=room, device=device, command=command)

    @staticmethod
    def __send_command(room, device, command):
        print("command", command)
        pylightwaverf.LightWaveRF().control(room, device, command)


    def pair(self):
        '''
        Call this once device is in pairing mode to pair the device
        '''
        self.state = DeviceState.STATE_ON

    @staticmethod
    def __createComand(val):
        kaku_val = (int(val) / 3) - 1
        if kaku_val < 1:
            command = DeviceState.STATE_OFF
        else:
            command = DeviceState.STATE_DIM + int(kaku_val)
        return command


