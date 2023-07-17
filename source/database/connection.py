from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, login, password, host, port, database):
        self.login = login
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.url = f'postgresql+psycopg2://{self.login}:{self.password}@{self.host}:{self.port}/{self.database}'
        self.engine = create_engine(self.url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None

    def connect(self):
        self.session = self.Session()
        return self.session

    def close(self):
        if self.session is not None:
            self.session.close()
            self.session = None
