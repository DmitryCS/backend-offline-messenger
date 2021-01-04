from api.request import RequestCreateUserDto, RequestGetUserDto, RequestPatchUserDto
from api.request.user import RequestPatchUserDtoSchema
from db.database import DBSession
from db.models import DBUser


def create_user(session: DBSession, user: RequestCreateUserDto) -> DBUser:
    new_user = DBUser(
        first_name=user.first_name,
        last_name=user.last_name,
        login=user.login,
        password=user.password,
    )

    session.add_model(new_user)

    return new_user


def get_user(session: DBSession, user: RequestGetUserDto) -> DBUser:

    user = session.query(DBUser).filter_by(login="andrew@gmail.com").first()

    return user


def patch_user(session: DBSession, user: RequestPatchUserDto) -> DBUser:

    user_dict = RequestPatchUserDtoSchema().dump(user)

    session.query(DBUser).filter(DBUser.login == 'andrew@gmail.com').update(user_dict)

    return DBUser()
