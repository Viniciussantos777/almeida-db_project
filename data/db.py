import sqlite3

DB_NAME = "almeida_db_project.db"

def get_connection():
    return sqlite3.connect(DB_NAME)
