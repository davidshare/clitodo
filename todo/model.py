import sqlite3
from database.database import SQLiteDatabase


class TodoModel:
    def __init__(self, db: SQLiteDatabase):
        self.db = db
        self.create_table()

    def check_table_exists(self):
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
            result = self.db.fetch_one(query)
            return result is not None
        except sqlite3.Error as e:
            print(f"Error checking if table exists: {e}")
            return False

    def create_table(self):
        """
        Create the todo table.
        Returns:
            bool: True if the table was created successfully, False otherwise.
        """
        table_exists = self.check_table_exists()
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
            self.db.execute_query(query)
        except sqlite3.Error as e:
            print(f"Error creating todos table: {e}")
