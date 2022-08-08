import typer

from linux_basic.command import Init
from linux_profile.utils.text import text_error, text_command

app = typer.Typer(help="Awesome CLI prifile manager.")


@app.command()
def init(param: str):
    try:
        Init(param=param)
    except Exception as error:
        text_error(value=error.args[0])

@app.command()
def pull(param: str):
    text_command(value='pull')


@app.command()
def push(param: str):
    text_command(value='push')


@app.command()
def commit(param: str):
    text_command(value='commit')


@app.command()
def apply(param: str):
    text_command(value='apply')


if __name__ == "__main__":
    app()
