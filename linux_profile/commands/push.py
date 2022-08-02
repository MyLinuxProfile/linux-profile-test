"""System Command"""

from linux_profile.config.command import BaseCommand
from linux_profile.utils.text import text_command


class Push(BaseCommand):
    """Start of settings
    """
    def start(self) -> None:
        """Start
        """
        try:
            self.load_config()
            self.load_profile()
        except Exception as error:
            raise Exception("It is not possible to load the basic settings.") from error

    def param_all(self):
        """Param All
        """
        text_command(value='push ' + self.param)
