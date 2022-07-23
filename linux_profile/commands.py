import configparser

from linux_profile.config import FILE_CONF
from linux_profile.utils import (
    get_system,
    get_distro,
    write_file
)


class Init(object):
    """
    Start of settings
    """

    def __init__(self, user: str, token: str):
        self.system = get_system()
        self.distro = get_distro()
        self.user = user
        self.token = token

    def add_user(self):
        """
        Add User
        """
        config = configparser.ConfigParser()

        config['SYSTEM'] = self.system
        config['DISTRO'] = self.distro
        config['DEFAULT'] = {
                'user': self.user,
                'token': self.token
            }

        write_file(path_file=FILE_CONF, config=config)

    def add_profile(profile_id: str):
        pass
