import configparser

from linux_profile.config import FILE_CONF
from linux_profile.utils.file import get_system, get_distro, write_file


class BaseAction(object):
    """Base class that defines how actions work
    """

    def __init__(self, user: str, token: str) -> None:
        """Construct the actions for profile

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

        self.setup()

    def setup(self):
        """Initial setup
        """
        try:
            self.system = get_system()
            self.distro = get_distro()
            self.add_config()

        except Exception as error:
            raise ValueError("It is not possible to create the basic settings.")

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
