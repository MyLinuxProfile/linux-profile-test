from os import path
from linux_profile.config.base import Config
from tests import (
    FOLDER_CONFIG,
    FOLDER_PROFILE,
    FILE_CONFIG,
    FILE_PROFILE
)


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
    
    

    test = Config(
        param='all',
        email='test@linuxprofile.com',
        token='token',
        file_config=FILE_CONFIG,
        file_profile=FILE_PROFILE,
        folder_config=FOLDER_CONFIG,
        folder_profile=FOLDER_PROFILE
    )

    test.set_folder()

    test.add_config()
    test.load_config()
    
    test.add_profile(profiles=profiles)
    test.load_profile()
    
    test.list_profile()
    test.set_profile(option='2')

    assert path.isdir(FOLDER_CONFIG) == True
    assert path.isdir(FOLDER_PROFILE) == True
    assert path.isfile(FILE_CONFIG) == True
    assert path.isfile(FILE_PROFILE) == True
    
    assert len(test.system) == 10
    assert len(test.distro) == 12

    assert len(test.profiles) == 2
    assert test.profiles[0]['profile_id'] == 'test_93e02be421d03bca'
    assert test.profiles[1]['profile_id'] == 'test_93e02be421d03bcb'
