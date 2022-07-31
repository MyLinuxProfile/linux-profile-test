from os import path
from linux_profile.config.base import BaseProfile
from linux_profile.config import (
    FOLDER_CONFIG,
    FOLDER_PROFILE,
    FILE_CONFIG,
    FILE_PROFILE
)


class Init(BaseProfile):
    """Start of settings
    """
    def __init__(self, 
                 email: str = None, 
                 token: str = None, 
                 param: str = None) -> None:
        self.email = email
        self.token = token
        self.param = param
        self.system = {}
        self.distro = {}
        self.profiles = []

    def param_all(self):
        """Param All
        """
        pass


def test_setup():

    profiles = [
        {
            "user_id": 2,
            "id": 2,
            "profile_id": "test_93e02be421d03bca"
        },
        {
            "user_id": 2,
            "id": 3,
            "profile_id": "test_93e02be421d03bcb"
        }
    ]

    test = Init(param='all', email='test@linuxprofile.com', token='token')
    test.setup_folder()

    test.setup_config()
    test.load_config()

    test.setup_profile(profiles=profiles)
    test.load_profile()

    assert path.isdir(FOLDER_CONFIG) == True
    assert path.isdir(FOLDER_PROFILE) == True
    assert path.isfile(FILE_CONFIG) == True
    assert path.isfile(FILE_PROFILE) == True
    
    assert len(test.system) == 10
    assert len(test.distro) == 12

    assert len(test.profiles) == 2
    assert test.profiles[0]['profile_id'] == 'test_93e02be421d03bca'
    assert test.profiles[1]['profile_id'] == 'test_93e02be421d03bcb'
