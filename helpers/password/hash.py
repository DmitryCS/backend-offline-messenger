import bcrypt

from helpers.password.exceptions import GeneratePasswordHashException, CheckPasswordHashException


def generate_hash(pwd: str) -> bytes:
    try:
        return bcrypt.hashpw(
            password=pwd.encode(),
            salt=bcrypt.gensalt(),
        )
    except (TypeError, ValueError) as e:
        raise GeneratePasswordHashException(str(e))


def check_hash(pwd: str, hsh: bytes) -> None:
    try:
        result = bcrypt.checkpw(
            password=pwd.encode(),
            hashed_password=hsh,
        )
    except (TypeError, ValueError) as e:
        raise CheckPasswordHashException(str(e))
    if not result:
        raise CheckPasswordHashException


if __name__ == '__main__':
    password = 'qwerty'
    password2 = 'qwerty'
    password3 = 'qwerty1'
    hsh_ = generate_hash(password)

    print(check_hash(password2, hsh_))
    print(check_hash(password3, hsh_))
