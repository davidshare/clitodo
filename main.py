from .database import SQLiteDatabase
from todo import Todo

if __name__ == "__main__":
    db = SQLiteDatabase("todo.db")
    db.connect()

    todo = Todo(
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
