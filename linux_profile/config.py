from os import getenv
from dotenv import load_dotenv

load_dotenv()

URL_API = getenv("URL_API")
FOLDER_CONFIG = '.config'
FOLDER_PROFILE = '.config/profiles'

FILE_CONFIG = '.config/linux_config.ini'
FILE_PROFILE = '.config/linux_profile.ini'

FILE_DISTRO = '.config/.os-release'
FILE_SYSTEM = '.config/.hostnamectl'
