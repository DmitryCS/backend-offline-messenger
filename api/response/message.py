from marshmallow import Schema, fields, pre_load, post_load

from api.base import ResponseDto
from db.models import DBMessage


class ResponseCreateMessageDtoSchema(Schema):
    id = fields.Int(required=True)
    sender_id = fields.Int(required=True)
    recipient_id = fields.Int(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)
    message = fields.Str(required=True)

    @pre_load
    @post_load
    def serialize_datetime(self, data: dict, **kwargs) -> dict:
        if 'created_at' in data:
            data['created_at'] = str(data['created_at'])
        if 'updated_at' in data:
            data['updated_at'] = str(data['updated_at'])

        return data


class ResponseCreateMessageDto(ResponseDto, ResponseCreateMessageDtoSchema):
    __schema__ = ResponseCreateMessageDtoSchema


class ResponseGetMessageDtoSchema(Schema):
    # messages = fields.List(DBMessage, required=True)
    id = fields.Int(required=True)
    sender_id = fields.Int(required=True)
    recipient_id = fields.Int(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)
    message = fields.Str(required=True)

    @pre_load
    @post_load
    def serialize_datetime(self, data: dict, **kwargs) -> dict:
        if 'created_at' in data:
            data['created_at'] = str(data['created_at'])
        if 'updated_at' in data:
            data['updated_at'] = str(data['updated_at'])

        return data


class ResponseGetMessageDto(ResponseDto, ResponseGetMessageDtoSchema):
    __schema__ = ResponseGetMessageDtoSchema


class ResponsePatchMessageDtoSchema(Schema):
    pass


class ResponsePatchMessageDto(ResponseDto, ResponsePatchMessageDtoSchema):
    __schema__ = ResponsePatchMessageDtoSchema


class ResponseDeleteMessageDtoSchema(Schema):
    pass


class ResponseDeleteMessageDto(ResponseDto, ResponseDeleteMessageDtoSchema):
    __schema__ = ResponseDeleteMessageDtoSchema
