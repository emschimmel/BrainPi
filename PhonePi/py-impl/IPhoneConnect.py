#https://github.com/picklepete/pyicloud

from datetime import datetime
from pyicloud import PyiCloudService
import sys
sys.path.append('../gen-py')
from AgendaPi.ttypes import GetItemsActionInput
from ThriftException.ttypes import ExternalEndpointUnavailable

class CalendarConnect:

    @classmethod
    def getEvents(self, input):
        input = self.__fixDefaultNones(input=input)
        try:
            api = PyiCloudService(input.email)
            from_dt = datetime(year=input.startYear, month=input.startMonth, day=input.startDay)
            to_dt = datetime(year=input.endYear, month=input.endMonth, day=input.endDay)
            output = api.calendar.events(from_dt, to_dt)
            return output
        except Exception as ex:
            print(ex)
            raise ExternalEndpointUnavailable("AgendaPi", "Device needs to be registered", "icloud")

    @staticmethod
    def __fixDefaultNones(input):
        current = datetime.utcnow()
        new_object = GetItemsActionInput()
        new_object.action = input.action
        new_object.email = input.email
        new_object.startDay = input.startDay if input.startDay is not None else current.day
        new_object.startMonth = input.startMonth if input.startMonth is not None else current.month
        new_object.startYear = input.startYear if input.startYear is not None else current.year
        new_object.endDay = input.endDay if input.endDay is not None else current.day
        new_object.endMonth = input.endMonth if input.endMonth is not None else current.month
        new_object.endYear = input.endYear if input.endYear is not None else current.year
        return new_object


