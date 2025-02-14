import sqlite3
from .database import SQLiteDatabase


class Todo:
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

        self.create_table(self.db)

    @classmethod
    def check_table_exists(cls, db: SQLiteDatabase):
        """
        Check if the todos table exists in the database
        Args:
        Returns:
            bool: True if table exists, False otherwise
        """
        query = """
        SELECT name from sqlite_master
        WHERE type='table'AND name='todos' 
        """
        try:
            result = db.fetch_one(query)
            return result is not None
        except sqlite3.Error as e:
            print(f"Error checking if table exists: {e}")
            return False

    @classmethod
    def create_table(cls, db: SQLiteDatabase):
        """
        Create the todo table.
        Returns:
            bool: True if the table was created successfully, False otherwise.
        """
        table_exists = cls.check_table_exists(db)
        if table_exists:
            print("Todo table already exists")
            return True

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
