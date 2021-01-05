from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseCreateUserDtoSchema(Schema):
    pass


class ResponseCreateUserDto(ResponseDto, ResponseCreateUserDtoSchema):
    __schema__ = ResponseCreateUserDtoSchema


class ResponseGetUserDtoSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    login = fields.Str(required=True)


class ResponseGetUserDto(ResponseDto, ResponseGetUserDtoSchema):
    __schema__ = ResponseGetUserDtoSchema


class ResponsePatchUserDtoSchema(Schema):
    pass


class ResponsePatchUserDto(ResponseDto, ResponsePatchUserDtoSchema):
    __schema__ = ResponsePatchUserDtoSchema
