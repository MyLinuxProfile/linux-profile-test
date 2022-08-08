"""System base"""

import logging
import configparser

from os import mkdir
from os.path import exists

from linux_profile.utils.file import get_system, get_distro, write_file_ini
from linux_profile.config import (
    FILE_CONFIG,
    FOLDER_CONFIG,
    FOLDER_PROFILE
)


class ValidationError(Exception):
    """Raised during the validation process of the config on errors.
    """

class ProcessingError(Exception):
    """Returns an exception during the execution of a process.
    """


class Config(object):
    """Configuration
    """

    LOG = logging.getLogger('.config/logs')

    def __init__(self,
                 email: str = '',
                 token: str = '',
                 param: str = None,
                 file_config: str = FILE_CONFIG,
                 folder_config: str = FOLDER_CONFIG,
                 folder_profile: str = FOLDER_PROFILE):
        """
        Structure that defines the main variables.
        """
        self.email = email
        self.token = token
        self.param = param

        self.file_config = file_config
        self.folder_config = folder_config
        self.folder_profile = folder_profile

        self.system = {}
        self.distro = {}
        self.user = {}

        self.setup()

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.set_folder()
        self.start()

    def start(self):
        """
        Defines functions that are executed separately
        when the class is instantiated.
        """
        self.add_config()
        self.load_config()

    def set_folder(self) -> None:
        """
        Setup Folder

        Checks and creates the structure of configuration
        folders that are used by the package.
        """
        if not exists(self.folder_config):
            mkdir(self.folder_config)

        if not exists(self.folder_profile):
            mkdir(self.folder_profile)

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

        write_file_ini(path_file=self.file_config, config=config)

    def load_config(self) -> None:
        """
        Load Config

        Loads basic configuration information for use
        in the application and internal operations.
        """
        config = configparser.ConfigParser()
        config.read(self.file_config)

        self.distro = None
        self.system = None
        self.user = None

        for section in config.sections():
            setattr(self, section.lower(), {})

            for key, val in config.items(section):
                new_config = getattr(self, section.lower())
                new_config.update({key: val})
