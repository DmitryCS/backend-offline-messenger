import pytest

from helpers.password import generate_hash, check_hash, CheckPasswordHashException


@pytest.fixture()
def password_data() -> dict:
    return {
        'password': 'qwerty',
        'password2': 'qwerty',
        'password3': 'qwerty1'
    }


def test_valid_password_hash(password_data):

    hsh_ = generate_hash(password_data['password2'])

    assert check_hash(password_data['password'], hsh_) is None


def test_invalid_password_hash(password_data):

    hsh_ = generate_hash(password_data['password3'])

    with pytest.raises(CheckPasswordHashException):
        check_hash(password_data['password'], hsh_)
