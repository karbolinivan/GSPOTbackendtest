from pydantic import BaseSettings


class ConnectionSettings(BaseSettings):
    host: str
    port: str
    database: str
    login: str
    password: str

    class Config:
        env_file_encoding = "utf-8"
