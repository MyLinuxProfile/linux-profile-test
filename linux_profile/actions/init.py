from linux_profile.base import BaseProfile
from linux_profile.utils.request import BaseRequest
from linux_profile.utils.text import text_command, table_options
from rich.console import Console
from rich.table import Table

class Init(BaseProfile):
    """Start of settings
    """

    def connect_user(self):
        """Connect User
        """
        request = InitRequest()
        response = request.make_get()

        if response.status_code == 200:
            text_command(value="Connect", desc="Server connection to get profiles.")
            self.add_profile(profiles=response.json())
            self.load_profile()

            # OpetionGeral(profiles=self.profiles)


class OpetionGeral(object):

    def __init__(self, profiles):
        self.profiles = profiles
        self.option_setup()

    def option_setup(self):
        table_options(
            question='Select an option from the list:',
            options=[
                'View profile list',
                'Select Profile',
                'Register new profile',
                'Exit'
            ],
            first_column="Decription"
        )
        input_option_action = input()

        if input_option_action == '1':
            self.view_profile_list()

            if self.profiles:
                print("• Select Profile")

                input_option_action = input()
                while input_option_action not in ['yes', 'no']:
                    print('• I NEED CONFIRMATION. yes/no?')
                    input_option_action = input()

                if input_option_action == 'yes':
                    self.option_setup()

        if input_option_action == '2':
            self.select_profile()

    def view_profile_list(self):
        """View Profile List
        """
        if self.profiles:
            console = Console()
            table = Table(show_header=True, header_style="white")
            table.add_column("#")
            table.add_column("Profile")

            for index, item in enumerate(self.profiles):
                table.add_row(str(index+1), item['profile_id'])

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
