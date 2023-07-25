import allure
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from source.database.config import ConnectionSettings


class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, path_settings):
        self.settings = ConnectionSettings(_env_file=path_settings)
        self.login = self.settings.login
        self.password = self.settings.password
        self.host = self.settings.host
        self.port = self.settings.port
        self.database = self.settings.database
        self.url = f'postgresql+psycopg2://{self.login}:{self.password}@{self.host}:{self.port}/{self.database}'
        self.engine = None
        self.session = None

    @allure.step('Connect to the database')
    def connect(self):
        self.engine = create_engine(self.url)
        self.session = Session(bind=self.engine)
        return self.session

    @allure.step('Disconnect from the database')
    def close(self):
        if self.session or self.engine is not None:
            self.session.close()
            self.engine.dispose()
            self.session = None
            self.engine = None
