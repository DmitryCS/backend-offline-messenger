from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseCreateMessageDtoSchema(Schema):
    pass


class ResponseCreateMessageDto(ResponseDto, ResponseCreateMessageDtoSchema):
    __schema__ = ResponseCreateMessageDtoSchema


class ResponseGetMessageDtoSchema(Schema):
    messages = fields.List(fields.Str, required=True)


class ResponseGetMessageDto(ResponseDto, ResponseGetMessageDtoSchema):
    __schema__ = ResponseGetMessageDtoSchema
