from json import loads
from linux_profile.config.base import Config
from tests.utils import (
    FOLDER_CONFIG,
    FOLDER_PROFILE,
    FILE_CONFIG,
    FILE_PROFILE
)
from linux_profile.utils.file import (
    get_distro,
    get_system,
    read_file
)


def test_get_system():
    Config(
        file_config=FILE_CONFIG,
        file_profile=FILE_PROFILE,
        folder_config=FOLDER_CONFIG,
        folder_profile=FOLDER_PROFILE
    )
    system = get_system()

    list_system = {
        'statichostname': True,
        'iconname': True,
        'chassis': True,
        'machineid': True,
        'bootid': True,
        'operatingsystem': True,
        'kernel': True,
        'architecture': True,
        'hardwarevendor': True,
        'hardwaremodel': True,
    }

    for item in system.keys():
        assert list_system.get(item) == True


def test_get_distro():
    Config(
        file_config=FILE_CONFIG,
        file_profile=FILE_PROFILE,
        folder_config=FOLDER_CONFIG,
        folder_profile=FOLDER_PROFILE
    )
    distro = get_distro()

    list_distro = {
        'pretty_name': True,
        'name': True,
        'version_id': True,
        'version': True,
        'version_codename': True,
        'id': True,
        'id_like': True,
        'home_url': True,
        'support_url': True,
        'bug_report_url': True,
        'privacy_policy_url': True,
        'ubuntu_codename': True
    }

    for item in distro.keys():
        assert list_distro.get(item) == True


def test_read_file():
    content = read_file(path_file='tests/utils/test_file', type_file='.json')
    content_json = loads(content)

    assert content_json["test_file"] == True
