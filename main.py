import typer

app = typer.Typer(help="Awesome CLI prifile manager.")


@app.command()
def init(user: str, token: str):
    print("init")

@app.command()
def sync():
    print("sync")


if __name__ == "__main__":
    app()
