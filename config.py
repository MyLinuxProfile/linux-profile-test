from os import system, path
import configparser

FILE_CONF = '.linuxprofile.ini'
FILE_DISTRO = '.os-release'
FILE_SYSTEM = '.hostnamectl'


def get_system():
    """
    Get System Information
    """
    my_config = dict()
    system('hostnamectl > ' + FILE_SYSTEM)

    with open(FILE_SYSTEM, 'r', encoding='utf8') as file_system:
        file_system = file_system.read()

    return get_content(file=file_system, separator=":")


def get_content(file: str, separator: str):
    """
    Get the contents of a file.

    Parameters
    ----------
    file : str
        Name of the file to be formatted.
    separator: str
        Content separator type. Example "=" or ":".

    Returns
    -------
    dict
        Dictionary with file contents.
    """

    my_info = dict()

    file_list = file.replace(' ', '|').replace('\n', ' ').split()
    for item in file_list:
        info_name = None
        info_value = None

        for index, value in enumerate(item):
            if value == separator:
                info_name = item[0:index].lower().replace('|', '')
                info_value = item[index+1:len(item)] \
                    .replace('"', '').replace('|', ' ')

                if info_value[0] == ' ':
                    info_value = info_value[1:len(info_value)]

                my_info.update({info_name: info_value})

    return my_info


def get_distro():
    """
    Get Linux distribution
    """
    system("cat /etc/os-release > " + FILE_DISTRO)

    with open(FILE_DISTRO, 'r', encoding='utf8') as file_distro:
        file_distro = file_distro.read()

    return get_content(file=file_distro, separator="=")


def read_file():
    """
    Read File
    """
    config = configparser.ConfigParser()
    return config.sections()


def write_file(config: configparser):
    """
    Write File
    """
    with open(FILE_CONF, 'w') as configfile:
        config.write(configfile)


class Init(object):
    """
    Start of settings
    """

    def __init__(self, user: str, token: str):
        self.system = get_system()
        self.distro = get_distro()
        self.user = user
        self.token = token

    def add_user(self):
        """
        Add User
        """
        config = configparser.ConfigParser()

        config['SYSTEM'] = self.system
        config['DISTRO'] = self.distro
        config['DEFAULT'] = {
                'user': self.user,
                'token': self.token
            }

        write_file(config)

    def add_profile(profile_id: str):
        pass
