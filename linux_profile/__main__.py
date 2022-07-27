import typer

from rich import print
from linux_profile.actions import Init, Push, Pull, Commit
from linux_profile.utils.text import (
    Text,
    text_command,
    text_error
)

app = typer.Typer(help="Awesome CLI prifile manager.")


@app.command()
def init(email: str, token: str):
    print(Text.HEADER)
    print(Text.SEPARATOR)
    text_command(value="init", desc="Initial setup of your profile files")
    try:
        start = Init(email=email, token=token)
        start.connect_user()

    except Exception as error:
        text_error(value=error.args[0])


@app.command()
def sync_pull(param: str):
    try:
        Pull(param=param)
    except Exception as error:
        text_error(value=error.args[0])


@app.command()
def sync_push(param: str):
    try:
        Push(param=param)
    except Exception as error:
        text_error(value=error.args[0])


@app.command()
def sync_commit(param: str):
    try:
        Commit(param=param)
    except Exception as error:
        text_error(value=error.args[0])


if __name__ == "__main__":
    app()
