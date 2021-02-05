# backend-offline-messenger
Backend part of messenger app. Specification [here](https://docs.google.com/document/d/1e6QAi3vTzmO9nysBArd1DNhIsXsx4eSHfu_T0eXkLuc/edit?usp=sharing).
All available url paths and methods are in [transport/sanic/routes.py](https://github.com/DmitryCS/backend-offline-messenger/blob/master/transport/sanic/routes.py).
## Core technology stack
Sanic, Marshmallow, SQLAlchemy, PostgreSQL
## Installation
1. <b>Via Docker (fastest)</b><br>
Clone the repository or just download [.env](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/.env), [Dockerfile](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/Dockerfile), [docker-compose.yaml](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/docker-compose.yaml) and execute `docker-compose up`. <br>
2. <b>Manually</b><br>
Clone the repository. Execute commands [init.sql](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/init.sql) in your PostgreSQL. In the terminal execute `pip install -r requierements.txt` and then `alembic upgrade head`. Change `POSTGRES_HOST` in [.env](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/.env) to `POSTGRES_HOST=0.0.0.0` and execute `python main.py`.
## Additional features
1. The ability to get and change user data by login.
2. In path /swagger you can see all possible routes.
3. <b>Added the ability to send files along with a message. A message can have many attachments, and one file can be attached to many messages, so a many-to-many relationship has been implemented through a table 'msgs_to_files'.</b><br>
## Database schema:
  ![alt text](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/examples/raw_images/database%20schema.png) 
## Examples:
  Example of `post /files`:
  ![alt text](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/examples/post%20files.png)
  <br>Example of `post /msg`:
  ![alt text](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/examples/post%20message.png)
  <br>Example of `get /files/3`:
  ![alt text](https://raw.githubusercontent.com/DmitryCS/backend-offline-messenger/master/examples/get%20file%20by%20his%20id_.png)
  
### Postman export of request examples [here](https://github.com/DmitryCS/backend-offline-messenger/blob/master/backend-offline-messenger.postman_collection.json).
