"""System command"""

from linux_profile.utils.text import text_command


class BaseCommand(object):
    """Base Command class
    """
    PARAM = ['all']

    def __init__(self, param: str = None):
        """
        Structure that defines the main variables.
        """
        self.param = param
        self.setup()

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.start()

    def start(self) -> None:
        """Start
        """
        try:
            self.initial_commands()
        except Exception as error:
            raise Exception("It is not possible to load the basic commands.") from error

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


class Init(BaseCommand):
    """Start of settings
    """

    PARAM = ['login', 'create']

    def param_login(self):
        """Param Login
        """
        text_command(value='init ' + self.param)

    def param_create(self):
        """Param Create
        """
        text_command(value='init ' + self.param)
