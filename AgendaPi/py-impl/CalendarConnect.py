#https://github.com/picklepete/pyicloud

from datetime import datetime
from pyicloud import PyiCloudService
import sys
sys.path.append('../gen-py')
from ThriftException.ttypes import ExternalEndpointUnavailable

class CalendarConnect:

    @staticmethod
    def getEvents(input):
        try:
            api = PyiCloudService(input.email)
            from_dt = datetime(year=input.startYear, month=input.startMonth, day=input.startDay)
            to_dt = datetime(year=input.endYear, month=input.endMonth, day=input.endDay)
            output = api.calendar.events(from_dt, to_dt)
            return output
        except Exception as ex:
            raise ExternalEndpointUnavailable("AgendaPi", "Device needs to be registered", "icloud")


