from linux_profile.base import BaseProfile
from linux_profile.utils.request import BaseRequest
from linux_profile.utils.text import text_command


class Init(BaseProfile):
    """Start of settings
    """

    PARAM = ['login', 'create']

    def param_login(self):
        """Param All
        """
        text_command(value='init ' + self.param)

    def param_create(self):
        """Param All
        """
        text_command(value='init ' + self.param)
