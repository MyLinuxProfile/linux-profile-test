"""System command"""

from linux_profile.config.base import Config
from linux_profile.config.profile import Profile


class BaseCommand(Config):
    """Base Command class
    """
    PARAM = ['all']

    def start(self) -> None:
        """Start
        """
        try:
            self.module = Profile()

            self.load_config()
            self.initial_commands()
        except Exception as error:
            raise Exception("It is not possible to load the basic settings.") from error

    def initial_commands(self) -> None:
        """
        Initial Commands

        Function that orchestrates the commands and executes
        the commands dynamically with the list of global
        parameters of the class.
        """
        if self.param:
            if self.param not in self.PARAM:
                raise Exception(
                    "Invalid parameter: " + self.param + " not exist!"
                    )

            getattr(self, 'param_'+self.param)()
