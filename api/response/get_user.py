from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseGetUserDtoSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    login = fields.Str(required=True)


class ResponseGetUserDto(ResponseDto, ResponseGetUserDtoSchema):
    __schema__ = ResponseGetUserDtoSchema
