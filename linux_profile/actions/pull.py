import re
from linux_profile.base import BaseProfile
from linux_profile.utils.request import BaseRequest
from linux_profile.utils.text import text_command


class Pull(BaseProfile):
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

        text_command(value='sync-pull ' + self.param)
        getattr(self, 'param_'+self.param)()

    def param_all(self):
        """Param All
        """
        if self.profiles:
            for profile in self.profiles:
                if profile.get('standard') == '1':

                    request = InitRequest()
                    response = request.make_get(url=request.url + '/' + profile.get('profile_id'))

                    print(response.json())


class InitRequest(BaseRequest):

    def url(self):
        self.url = self.path + "profiles"