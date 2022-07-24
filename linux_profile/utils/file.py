import configparser

from os import system
from linux_profile.config import FILE_DISTRO, FILE_SYSTEM


def get_content(path_file: str, separator: str):
    """
    Get the contents of a file.

    Parameters
    ----------
    path_file : str
        Name of the file to be formatted.
    separator: str
        Content separator type. Example "=" or ":".

    Returns
    -------
    dict
        Dictionary with file contents.
    """

    my_info = dict()

    file_list = path_file.replace(' ', '|').replace('\n', ' ').split()
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


def get_system():
    """
    Get System Information

    Parameters
    ----------
    No parameters

    Returns
    -------
    dict
        Dictionary with contents of the .hostnamectl file.
    """
    system('hostnamectl > ' + FILE_SYSTEM)

    with open(FILE_SYSTEM, 'r', encoding='utf8') as file_system:
        file_system = file_system.read()

    return get_content(path_file=file_system, separator=":")


def get_distro():
    """
    Get Linux distribution

    Parameters
    ----------
    No parameters

    Returns
    -------
    dict
        Dictionary with contents of the .os-release file.
    """
    system("cat /etc/os-release > " + FILE_DISTRO)

    with open(FILE_DISTRO, 'r', encoding='utf8') as file_distro:
        file_distro = file_distro.read()

    return get_content(path_file=file_distro, separator="=")


def read_file():
    """
    Read File

    Parameters
    ----------
    No parameters

    Returns
    -------
    Instance of ConfigParser class
    """
    config = configparser.ConfigParser()
    return config.sections()


def write_file(path_file: str, config: configparser):
    """
    Write File

    Parameters
    ----------
    path_file : str
        Name of the file to be formatted.
    config :
        Instance of ConfigParser class

    Returns
    -------
    No return
    """

    with open(path_file, 'w') as configfile:
        config.write(configfile)

