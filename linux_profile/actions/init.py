from linux_profile.base import BaseProfile
from linux_profile.utils.text import text_command, text_question


class Init(BaseProfile):
    """Start of settings
    """

    PARAM = ['login', 'create']

    def param_login(self):
        """Param Login
        """
        text_command(value='init ' + self.param)
        self.fake_login_user()

        # TODO: setup_profile()
        # TODO: load_profile()

    def param_create(self):
        """Param Create
        """
        text_command(value='init ' + self.param)
        self.fake_create_user()

        # TODO: setup_profile()
        # TODO: load_profile()

    #####-----------FAKE------------#####

    def fake_login_user(self):
        """Fake
        """
        print("E-mail:")
        input_option = input()

        print("Token:")
        input_option = input()


    def fake_create_user(self):
        """Fake
        """
        print("E-mail:")
        input_option = input()

    def fake_list_profile(self):
        """Fake
        """
        pass

    def fake_set_profile(self):
        """"Fake
        """
        pass

    #####-----------FAKE------------#####