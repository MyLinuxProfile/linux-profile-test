from linux_profile.base import BaseProfile
from linux_profile.utils.request import BaseRequest
from linux_profile.utils.text import text_command, text_question


class Init(BaseProfile):
    """Start of settings
    """

    PARAM = ['login', 'create']

    def param_login(self):
        """Param Login
        """
        self.login_user()

    def param_create(self):
        """Param Create
        """
        text_command(value='init ' + self.param)
        # TODO: fake_create_user()

    def login_user(self):
        """Fake
        """
        request = InitRequest()
        response = request.make_get()

        if response.status_code == 200:
            text_command(value='init ' + self.param, desc="Server connection to get profiles.")
            self.setup_profile(profiles=response.json())
            self.load_profile()

    #####-----------FAKE------------#####

    def fake_create_user(self):
        """Fake
        """
        pass

    def fake_list_profile(self):
        """Fake
        """
        pass

    def fake_set_profile(self):
        """"Fake
        """
        pass

    #####-----------FAKE------------#####


class InitRequest(BaseRequest):

    def url(self):
        self.url = self.path + "sync_profiles"
