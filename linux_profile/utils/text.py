from rich import print
from linux_profile import __version__, _name, _url, _logo


class Text(object):
    """Class with basic texts
    """

    VERSION = __version__
    NAME = _name
    LOGO = _logo
    URL = _url
    SEPARATOR = chr(95)*42
    HEADER = "[white]" + LOGO + "\n" + NAME + ": " + VERSION + "[/white]\nDocs: " + URL


def text_command(value: str = 'not found'):
    """Text command
    """
    print(Text.SEPARATOR)
    print("[bold white]Command: " + value + "[/bold white]")


def text_error(value: str):
    """Text error
    """
    print("[bold red]Error: [/bold red]" + value)

