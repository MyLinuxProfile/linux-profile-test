import configparser

from os import mkdir
from os.path import exists
from typing import List

from linux_profile.config import (
    FILE_CONFIG,
    FILE_PROFILE,
    FOLDER_CONFIG,
    FOLDER_PROFILE
)
from linux_profile.utils.text import text_command, text_error
from linux_profile.utils.file import (
    get_system,
    get_distro,
    write_file_ini
)

class BaseConfig(object):
    """BaseProfile class that defines config
    """
    def __init__(self) -> None:
        self.setup_config()

    def setup_folder(self) -> None:
        """Setup Folder
        """
        if not exists(FOLDER_CONFIG):
            mkdir(FOLDER_CONFIG)

        if not exists(FOLDER_PROFILE):
            mkdir(FOLDER_PROFILE)

    def setup_config(self):
        self.setup_folder()


class BaseProfile(object):
    """BaseProfile class that defines how actions work
    """
    PARAM = ['all']

    def __init__(self, 
                 email: str = None, 
                 token: str = None, 
                 param: str = None) -> None:
        """Construct the actions for profile

        Parameters
        ----------
        param: str
            Params

        Returns
        -------
        No return
        """
        text_command(value="init", desc="Initial setup of your profile files")

        self.param = param
        self.system = {}
        self.distro = {}
        self.user = {
            "email": email,
            "token": token
        }
        self.profiles = []

        self.setup_folder()
        self.setup()

    def setup_folder(self) -> None:
        """Setup Folder
        """
        if not exists(FOLDER_CONFIG):
            mkdir(FOLDER_CONFIG)

        if not exists(FOLDER_PROFILE):
            mkdir(FOLDER_PROFILE)

    def initial_commands(self) -> None:
        """Initial Commands
        """
        if self.param:
            if self.param not in self.PARAM:
                raise Exception("Invalid parameter: " + self.param + " not exist!")

            getattr(self, 'param_'+self.param)()

    def start(self) -> None:
        """Start
        """
        try:
            self.setup_config()
            self.load_config()
        except Exception as error:
            text_error(value=error.args[0])
            raise Exception("Not possible to start the basic settings.")

    def setup(self) -> None:
        """Initial setup
        """
        try:
            self.start()
            self.initial_commands()
        except Exception as error:
            text_error(value=error.args[0])
            raise Exception("Not possible to install the basic settings.")

    def setup_config(self) -> None:
        """Add Config
        """
        config = configparser.ConfigParser()
        config['SYSTEM'] = get_system()
        config['DISTRO'] = get_distro()
        config['USER'] = self.user

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

    def setup_profile(self, profiles: List) -> None:
        """Add Profile
        """
        config = configparser.ConfigParser()
        for item in profiles:
            item.update({"standard": 0})
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
