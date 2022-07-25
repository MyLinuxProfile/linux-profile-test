from linux_profile.base import BaseProfile
from linux_profile.utils.request import BaseRequest
from linux_profile.utils.text import text_command
from rich.console import Console
from rich.table import Table

class Init(BaseProfile):
    """Start of settings
    """
    def __init__(self, email: str, token: str):
        super().__init__(email, token)

    def connect_user(self):
        """Connect User
        """
        request = InitRequest()
        response = request.make_get()

        if response.status_code == 200:
            text_command(value="Connect", desc="Server connection to get profiles.")
            OpetionGeral(profiles=response.json())


class OpetionGeral(object):

    def __init__(self, profiles):
        self.profiles = profiles
        self.option_setup()

    def option_setup(self):
        console = Console()
        print("")
        print("• SELECT AN OPTION FROM THE LIST:")
        option_action = Table(show_header=True, header_style="white")
        option_action.add_column("Option")
        option_action.add_column("Decription")
        option_action.add_row(str(1), 'View profile list')
        option_action.add_row(str(2), 'Select Profile')
        option_action.add_row(str(3), 'Register new profile')
        option_action.add_row(str(4), 'Exit')
        console.print(option_action)
        input_option_action = input()

        if input_option_action == '1':
            self.view_profile_list()

            if self.profiles:
                print("• CONTINUE? yes/no")

                input_option_action = input()
                while input_option_action not in ['yes', 'no']:
                    print('• I NEED CONFIRMATION. yes/no?')
                    input_option_action = input()

                if input_option_action == 'yes':
                    self.option_setup()

        if input_option_action == '2':
            self.select_profile()

    def view_profile_list(self):
        if self.profiles:
            console = Console()
            table = Table(show_header=True, header_style="white")
            table.add_column("ID")
            table.add_column("Profile")

            for item in self.profiles:
                table.add_row(str(item['id']), item['profile_id'])

            console.print(table)
        
        else:
            print("• NO PROFILES. WANT TO CREATE ONE NOW? yes/no")
            input_option_action = input()

            while input_option_action not in ['yes', 'no']:
                print('• I NEED CONFIRMATION. yes/no?')
                input_option_action = input()

            if input_option_action == 'yes':
                self.register_new_profile()

    def select_profile(self):
        print('WHICH PROFILE DO YOU WANT TO SET?')
        input_option_action = input()

    def register_new_profile(self):
        pass


class InitRequest(BaseRequest):

    def url(self):
        self.url = self.path + "sync_profiles"
