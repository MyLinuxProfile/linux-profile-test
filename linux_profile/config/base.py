import logging
import configparser

from os import mkdir
from os.path import exists
from typing import List

from linux_profile.utils.file import get_system, get_distro, write_file_ini
from linux_profile.config import (
    FILE_CONFIG,
    FILE_PROFILE,
    FOLDER_CONFIG,
    FOLDER_PROFILE
)


class ValidationError(Exception):
    """Raised during the validation process of the config on errors.
    """


class Config(object):
    """Configuration
    """

    log = logging.getLogger('.config/logs')

    def __init__(self,
                 email: str = None,
                 token: str = None,
                 param: str = None):
        """
        Structure that defines the main variables.
        """
        self.email = email
        self.token = token
        self.param = param

        self.system = dict()
        self.distro = dict()
        self.user = dict()
        self.profiles = []

        self.setup()

    def setup(self):
        """
        Set to basic settings
        """
        self.set_folder()
        self.start()

    def start(self):
        """
        Start to basic settings
        """
        self.add_config()
        self.load_config()

    def set_folder(self) -> None:
        """
        Setup Folder

        Checks and creates the structure of configuration
        folders that are used by the package.
        """
        if not exists(FOLDER_CONFIG):
            mkdir(FOLDER_CONFIG)

        if not exists(FOLDER_PROFILE):
            mkdir(FOLDER_PROFILE)

    def add_config(self):
        """
        Configuring system settings

        Function that configures the basic settings of the
        operating system that the LinuxProfle package is running.

        Saved in the linux_config.ini configuration file more
        specifically Hardware and Distribution information.
        """
        config = configparser.ConfigParser()
        config['SYSTEM'] = get_system()
        config['DISTRO'] = get_distro()
        config['USER'] = {
            "email": self.email,
            "token": self.token
        }

        write_file_ini(path_file=FILE_CONFIG, config=config)

    def load_config(self) -> None:
        """
        Load Config

        Loads basic configuration information for use
        in the application and internal operations.
        """
        config = configparser.ConfigParser()
        config.read(FILE_CONFIG)

        self.distro = None
        self.system = None
        self.user = None

        for section in config.sections():
            setattr(self, section.lower(), {})

            for key, val in config.items(section):
                new_config = getattr(self, section.lower())
                new_config.update({key: val})

    def add_profile(self, profiles: List[dict]) -> None:
        """
        Add Profile

        Function that reads a list of profiles and saves
        default profile settings in linux_profile.ini.

        Parameters
        ----------
        profiles: List[dict]
            Exemple:
                profiles = [
                    {
                        "user_id": 1,
                        "profile_id": "key",
                        "id": 1
                    }
                ]
        """
        config = configparser.ConfigParser()
        for item in profiles:
            item.update({"standard": 0})
            config['PROFILE_' + str(item['id'])] = item

        write_file_ini(path_file=FILE_PROFILE, config=config)

    def load_profile(self) -> None:
        """
        Load Profile

        Load basic information from profiles for use in the
        application and internal operations.
        """
        config = configparser.ConfigParser()
        config.read(FILE_PROFILE)

        for section in config.sections():
            setattr(self, section.lower(), {})

            my_dict = {}
            for key, val in config.items(section):
                if section.find('PROFILE_') >= 0:
                    my_dict.update({key: val})

            if my_dict:
                self.profiles.append(my_dict)
