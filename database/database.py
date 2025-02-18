import sqlite3


class SQLiteDatabase:
    """Class to connect to sqlite database"""

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self) -> None:
        """
        Connect to the SQLite database.
            Returns:
                None: True if the connection was successful, False otherwise.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"Successfully connected to database {self.db_name}!!!")
        except sqlite3.Error as e:
            print(f"Error connecting to database {e}")
            raise e

    def execute_query(self, query, params=None) -> None:
        """
        Execute an SQL query.
        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Parameters for the query. Defaults to None.
        Returns:
            None: True if the query was executed successfully, False otherwise.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except sqlite3.Error as e:
            print(f"Error executing query {e}")

    def fetch_all(self, query: str, params=None) -> list:
        """
        Fetch all rows from a query.
        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Parameters for the query. Defaults to None.
        Returns:
            list: A list of rows fetched from the database, or an empty list if an error occurred.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return []

    def fetch_one(self, query: str, params=None) -> tuple:
        """
        Fetch a single row from a query.
        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Parameters for the query. Defaults to None.
        Returns:
            tuple: A single row fetched from the database, or None if an error occurred.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return None

    def close(self) -> None:
        """
        Close the database connection.
        Returns:
            None: True if the connection was closed successfully, False otherwise.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
        else:
            print("No database connection to close")
