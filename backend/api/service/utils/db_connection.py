from decouple import config

from psycopg2 import pool
from psycopg2.extensions import connection

def build_db_creds() -> dict:
    return {
        "dbname": config("POSTGRES_DB"),
        "user": config("POSTGRES_USER"),
        "password": config("POSTGRES_PASSWORD"),
        "host": config("POSTGRES_HOST"),
        "port": config("POSTGRES_PORT")
    }


def get_db_connection(creds: dict) -> connection :
    """This is a helper function to get a database connection"""
    conn_pool = pool.SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        **creds)

    return conn_pool.getconn()
