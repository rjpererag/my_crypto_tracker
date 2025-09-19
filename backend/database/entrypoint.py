from service.dbhandler import DBHandler, DBCredentials



def main() -> None:
    creds = DBCredentials(
        db_name="mydatabase",
        db_user="postgres",
        db_password="mypassword",
        db_port="5432",
    )

    handler = DBHandler(creds=creds)
    print(handler.test_connection())

if __name__ == "__main__":
    main()
