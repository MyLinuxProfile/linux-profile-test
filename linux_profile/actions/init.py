from linux_profile.base import BaseProfile
from linux_profile.utils.text import text_command


class Init(BaseProfile):
    """Start of settings
    """

    PARAM = ['login', 'create']

    def param_login(self):
        """Param Login
        """
        text_command(value='init ' + self.param)
        # TODO: fake_login_user()

    def param_create(self):
        """Param Create
        """
        text_command(value='init ' + self.param)
        # TODO: fake_create_user()

    #####-----------FAKE------------#####

    def fake_login_user(self):
        pass

    def fake_create_user(self):
        pass

    #####-----------FAKE------------#####