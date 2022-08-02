from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text as _Text

from typing import List
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

def text_question(value: str):
    """Text Question
    """
    panel = Panel(_Text("• "+value, justify="left"))
    print(panel)

def text_command(value: str = 'not found', desc: str = ''):
    """Text command
    """
    desc = '--' + desc if desc else ''
    print("[bold white]Command: " + value + "[/bold white] " + desc)

def text_info(value: str = 'not found', desc: str = ''):
    """Text command
    """
    desc = '--' + desc if desc else ''
    print("[bold blue]Info: " + "[/bold blue]" + desc)

def text_error(value: str):
    """Text error
    """
    print("[bold red]Error: [/bold red]" + value)

def table_options(first_column: str, options: List, question: str = None):
    """Table Options
    """
    console = Console()
    if question:
        text_question(value=question)

    option_action = Table(show_header=True, header_style="white")
    option_action.add_column("#")
    option_action.add_column(first_column)

    for index, item in enumerate(options):
        option_action.add_row(str(index+1), str(item))

    console.print(option_action)
