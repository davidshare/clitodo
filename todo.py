import sqlite3
from .database import SQLiteDatabase


class Todo:
    """Class to manage todos"""

    def __init__(self, title, description, due_date, status=0, priority=0, parent=None):
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.due_date = due_date
        self.parent = parent

    def create_table(self, db: SQLiteDatabase):
        """
        Create the todo table.
        Returns:
            bool: True if the table was created successfully, False otherwise.
        """
        query = """
            CREATE TABLE IF NOT EXISTS todos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                status INTEGER NOT NULL DEFAULT 0,
                priority INTEGER NOT NULL DEFAULT 0,
                due_date INTEGER NOT NULL,
                parent INTEGER DEFAULT 0
            )
        """

        try:
            db.execute_query(query)
        except sqlite3.Error as e:
            print(f"Error creating todos table: {e}")

    def save(self, db: SQLiteDatabase) -> int:
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
            db.execute_query(
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

            return db.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error saving todo: {e}")
            return -1
