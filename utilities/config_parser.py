import configparser

from CONSTANTS import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}/configurations/configuration.ini')
#config.read('C:\Users\User\Documents\GitHub\Andsnchenko_Homework22\configurations\configuration.ini')

class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_driver_id():
        return config.get('browser', 'browser_id')

    @staticmethod
    def get_password():
        user_name = config.get('user_info', 'user_name')
        password = config.get('user_info', 'password')
        return [user_name, password]

