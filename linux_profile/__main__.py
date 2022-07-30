import typer

from rich import print
from linux_profile.actions import Init, Push, Pull, Commit, Apply
from linux_profile.utils.text import (
    Text,
    text_command,
    text_error
)

app = typer.Typer(help="Awesome CLI prifile manager.")


@app.command()
def init(param: str):
    print(Text.HEADER)
    print(Text.SEPARATOR)
    try:
        Init(param=param)
    except Exception as error:
        text_error(value=error.args[0])


@app.command()
def pull(param: str):
    try:
        Pull(param=param)
    except Exception as error:
        text_error(value=error.args[0])


@app.command()
def push(param: str):
    try:
        Push(param=param)
    except Exception as error:
        text_error(value=error.args[0])


@app.command()
def commit(param: str):
    try:
        Commit(param=param)
    except Exception as error:
        text_error(value=error.args[0])


@app.command()
def apply(param: str):
    try:
        Apply(param=param)
    except Exception as error:
        text_error(value=error.args[0])


if __name__ == "__main__":
    app()
