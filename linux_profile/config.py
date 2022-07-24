from os import getenv
from dotenv import load_dotenv

load_dotenv()

URL_API = getenv("URL_API")
FILE_CONF = '.linuxprofile.ini'
FILE_DISTRO = '.os-release'
FILE_SYSTEM = '.hostnamectl'
