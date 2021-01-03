import os
from dotenv import load_dotenv

load_dotenv()


class SQLiteConfig:
    name = os.getenv('dbname', 'db2.sqlite')
    url = rf'sqlite:///{name}'
