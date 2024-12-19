import typer

from .what import what

app = typer.Type()
app.command(what)

if __name__ == '__main__':
    app()

