import datetime
import os

from dotenv import load_dotenv
import jwt

from helpers.auth.exceptions import ReadTokenException

load_dotenv()

secret = os.getenv('secret_key', 'SUPER_SECRET_KEY')
token_lifetime = int(os.getenv('token_lifetime_days', 1))


def create_token(payload: dict) -> str:
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=token_lifetime)
    return jwt.encode(payload, secret, algorithm='HS256')


def read_token(token: str) -> dict:
    try:
        return jwt.decode(token, secret, algorithms='HS256')
    except jwt.exceptions.PyJWTError:
        raise ReadTokenException
