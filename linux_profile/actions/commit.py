from linux_profile.base import BaseProfile
from linux_profile.utils.text import text_command


class Commit(BaseProfile):
    """Start of settings
    """
    def setup(self) -> None:
        """Initial setup
        """
        try:
            self.load_config()
            self.load_profile()
        except Exception as error:
            print(error)
            raise Exception("It is not possible to load the basic settings.")

        if self.param not in ['all']:
            raise Exception("Invalid parameter: " + self.param + " not exist!")

        text_command(value='sync-commit ' + self.param)
        getattr(self, 'param_'+self.param)()

    def param_all(self):
        """Param All
        """
        pass
