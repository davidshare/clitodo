import typer
from database.database import SQLiteDatabase

from todo.service import TodoService

app = typer.Typer()
db = SQLiteDatabase("todo.db")
db.connect()


@app.command()
def create_todo(
    title: str,
    description: str,
    due_date: int,
    status: int = 1,
    priority: int = 0,
    parent: int = None,
):
    """cli command to create todo"""
    todo = TodoService(
        title=title,
        description=description,
        due_date=due_date,
        status=status,
        priority=priority,
        parent=parent,
        db=db,
    )

    todo.save()
