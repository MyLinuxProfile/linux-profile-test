import typer

from rich import print
from linux_profile.actions import Init
from linux_profile.utils.text import (
    Text,
    text_command,
    text_error
)

app = typer.Typer(help="Awesome CLI prifile manager.")


@app.command()
def init(email: str, token: str):
    print(Text.HEADER)
    text_command(value="init")

    try:
        start = Init(email=email, token=token)

        start.connect_user()

    except Exception as error:
        text_error(value=error.args[0])

@app.command()
def sync_pull():
    text_command(value="sync-pull")


@app.command()
def sync_push():
    text_command(value="sync-push")


@app.command()
def sync_commit():
    text_command(value="sync-commit")


if __name__ == "__main__":
    app()
