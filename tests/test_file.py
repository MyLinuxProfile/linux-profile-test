from json import loads

from pytest import param
from linux_profile.base import BaseProfile
from linux_profile.utils.file import (
    get_distro,
    get_system,
    read_file
)


class Init(BaseProfile):
    """Start of settings
    """
    def param_all(self):
        """Param All
        """
        pass


def test_get_system():
    Init(param='all')
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
    Init(param='all')
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
