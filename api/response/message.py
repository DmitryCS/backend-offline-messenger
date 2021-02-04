from marshmallow import Schema, fields

from api.base import ResponseDto, Serialization


class MessageFields:
    id = fields.Int(required=True)
    sender_id = fields.Int(required=True)
    recipient_id = fields.Int(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)
    message = fields.Str(required=True)
    file_ids = fields.List(fields.Int)


class ResponseCreateMessageDtoSchema(Schema, MessageFields, Serialization):
    pass


class ResponseCreateMessageDto(ResponseDto, ResponseCreateMessageDtoSchema):
    __schema__ = ResponseCreateMessageDtoSchema


class ResponseGetMessageDtoSchema(Schema, MessageFields, Serialization):
    pass


class ResponseGetMessageDto(ResponseDto, ResponseGetMessageDtoSchema):
    __schema__ = ResponseGetMessageDtoSchema


class ResponsePatchMessageDtoSchema(Schema, MessageFields, Serialization):
    pass


class ResponsePatchMessageDto(ResponseDto, ResponsePatchMessageDtoSchema):
    __schema__ = ResponsePatchMessageDtoSchema


class ResponseDeleteMessageDtoSchema(Schema):
    pass


class ResponseDeleteMessageDto(ResponseDto, ResponseDeleteMessageDtoSchema):
    __schema__ = ResponseDeleteMessageDtoSchema
