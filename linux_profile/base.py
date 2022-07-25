import configparser

from linux_profile.config import FILE_CONF
from linux_profile.utils.file import get_system, get_distro, write_file


class BaseProfile(object):
    """BaseProfile class that defines how actions work
    """

    def __init__(self, email: str = None, token: str = None) -> None:
        """Construct the actions for profile

        Parameters
        ----------
        email : str
            E-mail
        token: str
            User access token

        Returns
        -------
        No return
        """
        self.user = {
            'email': email,
            'token': token
        }

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
        config['USER'] = self.user

        write_file(path_file=FILE_CONF, config=config)

    def load_config(self) -> None:
        """Load Config
        """
        config = configparser.ConfigParser()
        config.read(FILE_CONF)
        
        self.distro = None
        self.system = None
        self.user = None

        for section in config.sections():
            setattr(self, section.lower(), {}) 

            for key, val in config.items(section):
                new_config = getattr(self, section.lower())
                new_config.update({key: val})
