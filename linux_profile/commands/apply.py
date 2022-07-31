from linux_profile.config.base import BaseProfile
from linux_profile.utils.text import text_command


class Apply(BaseProfile):
    """Start of settings
    """
    def start(self) -> None:
        """Start
        """
        try:
            self.load_config()
            self.load_profile()
        except Exception as error:
            print(error)
            raise Exception("It is not possible to load the basic settings.")

    def param_all(self):
        """Param All
        """
        text_command(value='apply ' + self.param)
