from psycopg2 import pool
from psycopg2.extensions import connection

def build_db_creds() -> dict:  # TODO CHANGE TO USE ENV VARIABLES
    return {
        "dbname": "postgres",
        "user": "postgres",
        "password": "mypassword",
        "host": "db",
        "port": "5432"
    }


def get_db_connection(creds: dict) -> connection :
    """This is a helper function to get a database connection"""
    conn_pool = pool.SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        **creds)

    return conn_pool.getconn()
