from GenericStruct.ttypes import ActionEnum
from AutorisationStruct.ttypes import Autorisation
from WeatherPi.ttypes import WeatherInput
from AgendaPi.ttypes import ConfigItem as AgendaConfigStruct
from PhotoPi.ttypes import ConfigItem as PhotoConfigStruct
from MusicPi.ttypes import ConfigItem as MusicConfigStruct

import pickle

class AutorisationsStructProvider:

    @classmethod
    def generate_full_autorisations(self):
        autorisations = dict()
        autorisations[ActionEnum.LOGIN] = self.__login_autorisations()
        autorisations[ActionEnum.LIGHT] = self.__light_autorisations()
        autorisations[ActionEnum.AGENDA] = self.__agenda_autorisations()
        autorisations[ActionEnum.MUSIC] = self.__music_autorisations()
        autorisations[ActionEnum.WEATHER] = self.__weather_autorisations()
        autorisations[ActionEnum.CONFIG] = self.__config_autorisations()
        autorisations[ActionEnum.PHOTO] = self.__photo_autorisations()
        return autorisations

    @staticmethod
    def __login_autorisations():
        loginautorisation = Autorisation()
        loginautorisation.enabled = True
        return loginautorisation

    @staticmethod
    def __light_autorisations():
        lightautorisation = Autorisation()
        lightautorisation.enabled = True
        # TODO: check if stateless
        return lightautorisation

    @staticmethod
    def __agenda_autorisations():
        agendaautorisation = Autorisation()
        agendaautorisation.enabled = True
        agenda_config = AgendaConfigStruct()
        agenda_config.email = "we.rule@icloud.com"
        agendaautorisation.module_config = pickle.dumps(obj=agenda_config, protocol=None, fix_imports=False)
        return agendaautorisation

    @staticmethod
    def __music_autorisations():
        musicautorisation = Autorisation()
        musicautorisation.enabled = True
        music_config = MusicConfigStruct()
        music_config.email = "we.rule@icloud.com"
        musicautorisation.module_config = pickle.dumps(obj=music_config, protocol=None, fix_imports=False)
        return musicautorisation

    @staticmethod
    def __weather_autorisations():
        weatherautorisation = Autorisation()
        weatherautorisation.enabled = True
        weather_input = WeatherInput()
        weather_input.location = 'Amsterdam,nl'
        weatherautorisation.module_config = pickle.dumps(obj=weather_input, protocol=None, fix_imports=False)
        return weatherautorisation

    @staticmethod
    def __config_autorisations():
        configautorisation = Autorisation()
        configautorisation.enabled = True
        return configautorisation

    @staticmethod
    def __photo_autorisations():
        photoautorisation = Autorisation()
        photoautorisation.enabled = True
        photo_config = PhotoConfigStruct()
        photo_config.email = "we.rule@icloud.com"
        photoautorisation.module_config = pickle.dumps(obj=photo_config, protocol=None, fix_imports=False)
        return photoautorisation
