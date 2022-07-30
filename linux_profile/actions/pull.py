from linux_profile.base import BaseProfile
from linux_profile.utils.request import BaseRequest
from linux_profile.utils.text import text_command, text_question, text_info


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
        getattr(self, 'test_flow_'+self.param)()

    def test_flow_all(self):
        """
        """
        profiles = True

        text_info(desc='Connect to the server to get the profile')

        if profiles:
            # TODO: fake_download_profile()
            text_info(desc='Profile successfully updated!')
        else:
            text_question(value="You don't have profiles! Do you want to create? yes/no")
            input_action = input()

            while input_action not in ['yes', 'no']:
                text_question(value="I need confirmation. yes/no?")
                input_action = input()

            if input_action == 'yes':
                pass
                # TODO: fake_create_profile()

            if input_action == 'no':
                pass
                # TODO: fake_exit()

    def param_all(self):
        """Param All
        """
        if self.profiles:
            for profile in self.profiles:
                if profile.get('standard') == '1':

                    request = InitRequest()
                    response = request.make_get(url=request.url + '/' + profile.get('profile_id'))

                    print(response.json())

        else:
            print("• You don't have profiles!")


class InitRequest(BaseRequest):

    def url(self):
        self.url = self.path + "profiles"