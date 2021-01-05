from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateUserDtoSchema(Schema):
    first_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)
    login = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)


class RequestCreateUserDto(RequestDto, RequestCreateUserDtoSchema):
    __schema__ = RequestCreateUserDtoSchema


class RequestGetUserDtoSchema(Schema):
    pass


class RequestGetUserDto(RequestDto, RequestGetUserDtoSchema):
    __schema__ = RequestGetUserDtoSchema


class RequestPatchUserDtoSchema(Schema):
    first_name = fields.Str(required=False, allow_none=False)
    last_name = fields.Str(required=False, allow_none=False)
    password = fields.Str(required=False, allow_none=False)


class RequestPatchUserDto(RequestDto, RequestPatchUserDtoSchema):
    __schema__ = RequestPatchUserDtoSchema
