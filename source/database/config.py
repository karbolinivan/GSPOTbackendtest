from pydantic import BaseSettings


class ConnectionSettings(BaseSettings):
    host: str = "127.0.0.1"
    port: str = "5433"
    database: str = "test"
    login: str = "postgres"
    password: str = "password"
