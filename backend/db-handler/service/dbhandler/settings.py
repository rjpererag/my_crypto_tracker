from dataclasses import dataclass


@dataclass
class DBCredentials:
    db_name: str = None
    db_user: str = None
    db_password: str = None
    db_port: str = None