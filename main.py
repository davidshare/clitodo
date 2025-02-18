from database.database import SQLiteDatabase
from todo.service import TodoService
import typer

if __name__ == "__main__":
    db = SQLiteDatabase("todo.db")
    db.connect()

    todo = TodoService(
        title="Finish project",
        description="Complete the project by the deadline",
        due_date=1633072800,
        status=1,
        priority=2,
        parent=None,
        db=db,
    )
    todo.save()
    db.close()

    typer.echo("This is typer")
