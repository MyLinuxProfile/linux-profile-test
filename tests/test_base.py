from os import path
from linux_profile.config.base import Config
from linux_profile.config.profile import Profile
from tests import (
    FOLDER_CONFIG,
    FOLDER_PROFILE,
    FILE_CONFIG,
    FILE_PROFILE
)


def test_setup_config():
    
    test_config = Config(
        param='all',
        email='test@linuxprofile.com',
        token='token',
        file_config=FILE_CONFIG,
        folder_config=FOLDER_CONFIG,
        folder_profile=FOLDER_PROFILE
    )

    test_config.set_folder()
    test_config.add_config()
    test_config.load_config()

    assert path.isdir(FOLDER_CONFIG) == True
    assert path.isfile(FILE_CONFIG) == True
    
    assert len(test_config.system) == 10
    assert len(test_config.distro) == 12


def test_setup_profile():

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

    test_profile = Profile(
        file_profile=FILE_PROFILE
    )

    test_profile.add_profile(profiles=profiles)
    test_profile.load_profile()
    
    test_profile.list_profile()
    test_profile.set_profile(option='2')

    assert path.isfile(FILE_PROFILE) == True
    assert path.isdir(FOLDER_PROFILE) == True

    assert len(test_profile.profiles) == 2
    assert test_profile.profiles[0]['profile_id'] == 'test_93e02be421d03bca'
    assert test_profile.profiles[1]['profile_id'] == 'test_93e02be421d03bcb'
