from marshmallow import Schema, fields

from api.base import RequestDto


class RequestAuthUserDtoSchema(Schema):
    login = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)


class RequestAuthUserDto(RequestDto, RequestAuthUserDtoSchema):
    __schema__ = RequestAuthUserDtoSchema


class AuthResponseObject:
    def __init__(self, token):
        self.Authorization = token
