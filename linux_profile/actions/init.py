import configparser

from linux_profile.config import FILE_CONF
from linux_profile.utils import (
    get_system,
    get_distro,
    write_file
)


class Init(object):
    """Start of settings
    """

    def __init__(self, user: str, token: str):
        """
        Constructor

        Parameters
        ----------
        user : str
            Username
        token: str
            User access token

        Returns
        -------
        No return
        """

        self.user = user
        self.token = token

        self.run()

    def run(self):
        """Run
        """
        self.system = get_system()
        self.distro = get_distro()
        self.add_config()


    def add_config(self):
        """Add Config
        """
        config = configparser.ConfigParser()

        config['SYSTEM'] = self.system
        config['DISTRO'] = self.distro
        config['DEFAULT'] = {
                'user': self.user,
                'token': self.token
            }

        write_file(path_file=FILE_CONF, config=config)


    def connect_user(self):
        """Connect User
        """
        pass


    def add_profile(profile_id: str):
        pass

