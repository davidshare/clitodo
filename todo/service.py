import sqlite3
from database.database import SQLiteDatabase
from todo.model import TodoModel


class TodoService:
    """Class to manage todos"""

    def __init__(
        self,
        db: SQLiteDatabase,
        title: str,
        description: str,
        due_date: int,
        status: int = 0,
        priority: int = 0,
        parent: int = None,
    ):
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.due_date = due_date
        self.parent = parent
        self.db = db
        self.todo_model = TodoModel(self.db)
        self.todo_model.create_table()

    def save(self) -> int:
        """
        Save the todo item to the database.
        Returns:
            int: The ID of the newly inserted row, or -1 if an error occurred.
        """
        query = """
            INSERT INTO todos (title, description, status, priority, due_date, parent)
            values(?, ?, ?, ?, ?, ?)
        """

        try:
            self.db.execute_query(
                query,
                (
                    self.title,
                    self.description,
                    self.status,
                    self.priority,
                    self.due_date,
                    self.parent,
                ),
            )

            return self.db.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error saving todo: {e}")
            return -1
