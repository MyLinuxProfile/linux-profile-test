import typer
from linux_profile.commands import Init

app = typer.Typer(help="Awesome CLI prifile manager.")


@app.command()
def init(user: str, token: str):
    start = Init(user, token)
    start.add_user()

@app.command()
def sync():
    print("sync")


if __name__ == "__main__":
    app()
