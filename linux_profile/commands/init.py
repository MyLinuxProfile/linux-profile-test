from linux_profile.config.base import BaseProfile
from linux_profile.utils.request import BaseRequest
from linux_profile.utils.text import text_command, text_question


class Init(BaseProfile):
    """Start of settings
    """

    PARAM = ['login', 'create']

    def param_login(self):
        """Param Login
        """
        text_command(value='init ' + self.param)
        self.login_user()

    def param_create(self):
        """Param Create
        """
        text_command(value='init ' + self.param)
        self.create_user()

    def login_user(self):
        """Login User
        """
        request = InitRequest()
        response = request.make_get()

        if response.status_code == 200:
            self.setup_profile(profiles=response.json())
            self.load_profile()

    def create_user(self):
        """Create User
        """
        pass

    def list_profile(self):
        """List Profile
        """
        pass

    def set_profile(self):
        """"Set Profile
        """
        pass


class InitRequest(BaseRequest):

    def url(self):
        self.url = self.path + "sync_profiles"
