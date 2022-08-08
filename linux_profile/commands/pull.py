"""System Command"""

from linux_profile.config.command import BaseCommand
from linux_profile.utils.text import text_command


class Pull(BaseCommand):
    """Start of settings
    """

    def param_all(self):
        """Param All
        """
        text_command(value='pull ' + self.param)
        self.module.pull_profile()
