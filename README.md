# backend-offline-messenger
Backend part of messenger app. Specification [here](https://docs.google.com/document/d/1e6QAi3vTzmO9nysBArd1DNhIsXsx4eSHfu_T0eXkLuc/edit?usp=sharing).
All available url paths and methods are in [transport/sanic/routes.py](https://github.com/DmitryCS/backend-offline-messenger/blob/master/transport/sanic/routes.py).
## Core technology stack
Sanic, Marshmallow, SQLAlchemy, PostgreSQL
## Installation
1. <b>Via Docker (fastest)</b><br>
Clone the repository or just download [.env](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/.env), [Dockerfile](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/Dockerfile), [docker-compose.yaml](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/docker-compose.yaml) and execute `docker-compose up`. <br>
2. <b>Locally</b><br>
Clone the repository. Execute commands [init.sql](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/init.sql) in your PostgreSQL. In the terminal execute `pip install -r requierements.txt` and then `alembic upgrade head`. Change `POSTGRES_HOST` in [.env](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/.env) to `POSTGRES_HOST=0.0.0.0` and execute `python main.py`.
## Additional features
1. The ability to get and change user data by login.
2. In path /swagger you can see all possible routes.
### Postman export of request examples [here](https://github.com/DmitryCS/backend-offline-messenger/blob/master/backend-offline-messenger.postman_collection.json).