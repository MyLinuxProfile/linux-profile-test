import typer
from linux_profile import __logo__, __version__
from linux_profile.actions import Init

app = typer.Typer(help="Awesome CLI prifile manager.")


@app.command()
def init(user: str, token: str):
    start = Init(user, token)
    print(__logo__)
    print("My Linux Profile: v" + str(__version__))
    print("Docs: https://github.com/MyLinuxProfile/linux-profile-pypi/")


@app.command()
def sync_pull():
    print("sync_pull")


@app.command()
def sync_push():
    print("sync_push")


@app.command()
def sync_commit():
    print("sync_commit")


if __name__ == "__main__":
    app()
