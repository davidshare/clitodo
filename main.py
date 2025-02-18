import typer
from todo.cli import app as todo_cli

app = typer.Typer()

if __name__ == "__main__":
    typer.echo("This is typer")

app.add_typer(todo_cli, name="todo")
