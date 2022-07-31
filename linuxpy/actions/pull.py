from linuxpy.base import BaseProfile
from linuxpy.utils.text import text_command


class Pull(BaseProfile):
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
        text_command(value='pull ' + self.param)