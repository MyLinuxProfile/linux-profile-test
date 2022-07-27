import configparser

from os import mkdir
from os.path import exists

from typing import List
from linux_profile.config import FILE_CONFIG, FILE_PROFILE, FOLDER_CONFIG, FOLDER_PROFILE
from linux_profile.utils.file import get_system, get_distro, write_file_ini, write_file


class BaseProfile(object):
    """BaseProfile class that defines how actions work
    """

    def __init__(self, email: str = None, token: str = None, param: str = None) -> None:
        """Construct the actions for profile

        Parameters
        ----------
        email : str
            E-mail
        token: str
            User access token
        param: str
            Params

        Returns
        -------
        No return
        """
        if not exists(FOLDER_CONFIG):
            mkdir(FOLDER_CONFIG)

        if not exists(FOLDER_PROFILE):
            mkdir(FOLDER_PROFILE)

        self.email = email
        self.token = token
        self.param = param
        self.system = {}
        self.distro = {}
        self.user = {}
        self.profiles = []

        self.setup()

    def setup(self) -> None:
        """Initial setup
        """
        try:
            self.system = get_system()
            self.distro = get_distro()
            self.add_config()
            self.load_config()
        except Exception as error:
            print(error)
            raise ValueError("It is not possible to create the basic settings.")

    def add_config(self) -> None:
        """Add Config
        """
        config = configparser.ConfigParser()

        config['SYSTEM'] = self.system
        config['DISTRO'] = self.distro
        config['USER'] = {
            'email': self.email,
            'token': self.token
        }

        write_file_ini(path_file=FILE_CONFIG, config=config)

    def load_config(self) -> None:
        """Load Config
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

    def add_profile(self, profiles: List) -> None:
        """Add Profile
        """
        config = configparser.ConfigParser()

        for item in profiles:
            config['PROFILE_' + str(item['id'])] = item

        write_file_ini(path_file=FILE_PROFILE, config=config)

    def load_profile(self) -> None:
        """Load Profile
        """
        config = configparser.ConfigParser()
        config.read(FILE_PROFILE)
        
        self.profiles = []

        for section in config.sections():
            setattr(self, section.lower(), {})

            my_dict = {}
            for key, val in config.items(section):
                if section.find('PROFILE_') >= 0:
                    my_dict.update({key: val})

            if my_dict:
                self.profiles.append(my_dict)
