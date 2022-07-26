"""System Command"""

from linux_profile.utils.request import BaseRequest
from linux_profile.utils.text import text_command
from linux_profile.config.command import BaseCommand

from linux_profile.config.profile import Profile


class Init(BaseCommand):
    """Start of settings
    """

    PARAM = ['login', 'create']

    def start(self) -> None:
        """Start
        """
        try:
            self.module = Profile()

            self.add_config()
            self.load_config()
            self.initial_commands()
        except Exception as error:
            raise Exception("It is not possible to load the basic settings.") from error

    def param_login(self):
        """Param Login
        """
        text_command(value='init ' + self.param)
        self.module.add_profile()

    def param_create(self):
        """Param Create
        """
        text_command(value='init ' + self.param)


class InitRequest(BaseRequest):

    def url(self):
        self.url = self.path + "sync_profiles"
