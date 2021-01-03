from marshmallow import Schema

from api.base import RequestDto


class RequestGetUserDtoSchema(Schema):
    pass


class RequestGetUserDto(RequestDto, RequestGetUserDtoSchema):
    __schema__ = RequestGetUserDtoSchema
