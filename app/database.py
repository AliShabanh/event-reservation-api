import sqlite3

DATABASE_NAME = "event_reservation.db"

def connect_to_database():
    connection = sqlite3.connect(DATABASE_NAME)

    # Allows databse rows to be accessed by column name
    connection.row_factory = sqlite3.Row

    # Used to enable foreign key constraints, because SQLite does not enforce them by default
    # This makes sure a foreign key relationships are checked when inserting or updating data.
    connection.execute("PRAGMA foreign_keys = ON")

    return connection


def create_database():
    connection = connect_to_database()

    with open("docs/schema.sql", "r") as schema_file:
        schema = schema_file.read()

    # used to execute more then one SQL statement at a time.
    connection.executescript(schema)
    connection.commit()
    connection.close()
