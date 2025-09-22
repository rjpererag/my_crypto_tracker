from .settings import DBCredentials
from ..utils import logger

from psycopg2 import pool, OperationalError
from psycopg2.extensions import connection


class DBHandler:

    def __init__(self, creds: DBCredentials) -> None:

        self.db_params = {
            "dbname": creds.db_name,
            "user": creds.db_user,
            "password": creds.db_password,
            "host": "localhost",
            "port": creds.db_port
        }

        self.pool = self._create_connection_pool()

    def _create_connection_pool(self) -> pool.SimpleConnectionPool | None:
        try:
            conn = pool.SimpleConnectionPool(1, 10, **self.db_params)
            logger.info("Connection pool created successfully")

        except OperationalError as e:
            logger.info(f"Error creating connection pool, {str(e)}")
            conn = None

        return conn

    def get_conn(self) -> connection | None:
        if self.pool:
            return self.pool.getconn()

        else:
            logger.error(f"No pool to connect")
            return None

    def select(self, query: str, *args):
        if conn := self.get_conn():

            try:
                with conn.cursor() as cursor:
                    cursor.execute(query)

                    if args:
                        if args[0] == "fetchone":
                            results = cursor.fetchone()

                        elif args[0] == "fetchmany":
                            results = cursor.fetchmany()

                        else:
                            results = cursor.fetchall()

                    conn.close()
                    return results

            except Exception as e:
                logger.error(f"Error while selecting: {query}. {str(e)}")

            finally:
                self.pool.putconn(conn)

    def execute_query(self, query, params=None):
        """Executes a query within a transaction ensuring ACID compliance."""
        conn = self.get_conn()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            cursor.close()
            logger.info("Successfully inserted")
        except Exception as e:
            conn.rollback()
            logger.error(f"Error executing query: {e}. Query: {query}, Params: {params}")
        finally:
            if conn:
                self.pool.putconn(conn)

    def test_connection(self):
        if conn := self.get_conn():
            with conn.cursor() as cursor:
                query = "SELECT version () ;"
                cursor.execute(query)
                results = cursor.fetchall()
                self.pool.putconn(conn=conn)
                print(results)