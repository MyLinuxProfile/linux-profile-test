"""Profile base"""

import configparser

from typing import List

from linux_profile.utils.text import table_options
from linux_profile.utils.file import write_file_ini
from linux_profile.utils.request import BaseRequest

from linux_profile.config.base import ProcessingError
from linux_profile.config import FILE_PROFILE


class Profile(object):
    """Configuration
    """

    def __init__(self, file_profile: str = FILE_PROFILE):
        """
        Structure that defines the main variables.
        """
        self.file_profile = file_profile
        self.load_profile()

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

        write_file_ini(path_file=self.file_profile, config=config)

    def load_profile(self) -> None:
        """
        Load Profile

        Load basic information from profiles for use in the
        application and internal operations.
        """
        self.profiles = []

        config = configparser.ConfigParser()
        config.read(self.file_profile)

        for section in config.sections():
            setattr(self, section.lower(), {})

            my_dict = {}
            for key, val in config.items(section):
                if section.find('PROFILE_') >= 0:
                    my_dict.update({key: val})

            if my_dict:
                self.profiles.append(my_dict)

    def list_profile(self) -> None:
        """List Profile
        """
        options = []
        for item in self.profiles:
            options.append(item['profile_id'])

        table_options(
            question="",
            first_column="Profile",
            options=options
        )

    def set_profile(self, option: int) -> None:
        """"Set Profile
        """
        option = int(option)

        if option > 0 and option <= len(self.profiles):
            config = configparser.ConfigParser()
            config.read(self.file_profile)

            for section in config.sections():
                config[section]['standard'] = '0'

            profile = config.sections()[int(option)-1]
            config[profile]['standard'] = '1'

            write_file_ini(path_file=self.file_profile, config=config)
        else:
            raise ProcessingError()

    def pull_profile(self) -> None:
        """Pull Profile
        """
        request = ProfileRequest()

        if self.profiles:
            for profile in self.profiles:
                request.make_get(id=profile['profile_id'])


class ProfileRequest(BaseRequest):

    def url(self):
        self.url = self.path + "profiles"
