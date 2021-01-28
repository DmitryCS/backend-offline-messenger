from marshmallow import Schema, fields

from api.base import ResponseDto, Serialization


class UserFields:
    id = fields.Int(required=True)
    login = fields.Str(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)


class ResponseCreateUserDtoSchema(Schema, UserFields, Serialization):
    pass


class ResponseCreateUserDto(ResponseDto, ResponseCreateUserDtoSchema):
    __schema__ = ResponseCreateUserDtoSchema


class ResponseGetUserDtoSchema(Schema, Serialization):
    login = fields.Str(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)


class ResponseGetUserDto(ResponseDto, ResponseGetUserDtoSchema):
    __schema__ = ResponseGetUserDtoSchema


class ResponsePatchUserDtoSchema(Schema, UserFields, Serialization):
    pass


class ResponsePatchUserDto(ResponseDto, ResponsePatchUserDtoSchema):
    __schema__ = ResponsePatchUserDtoSchema
