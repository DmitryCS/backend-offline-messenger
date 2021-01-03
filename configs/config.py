from db.config import SQLiteConfig
from transport.sanic.config import SanicConfig


class ApplicationConfig:
    sanic: SanicConfig
    database: SQLiteConfig

    def __init__(self):
        self.sanic = SanicConfig()
        self.database = SQLiteConfig()
