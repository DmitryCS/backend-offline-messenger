from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateMessageDtoSchema(Schema):
    message = fields.Str(required=True, allow_none=False)
    recipient = fields.Str(required=True, allow_none=False)
    file_ids = fields.List(fields.Int)


class RequestCreateMessageDto(RequestDto, RequestCreateMessageDtoSchema):
    __schema__ = RequestCreateMessageDtoSchema


class RequestGetMessageDtoSchema(Schema):
    pass


class RequestGetMessageDto(RequestDto, RequestGetMessageDtoSchema):
    __schema__ = RequestGetMessageDtoSchema


class RequestPatchMessageDtoSchema(Schema):
    message = fields.Str(required=True, allow_none=False)
    file_ids = fields.List(fields.Int)


class RequestPatchMessageDto(RequestDto, RequestPatchMessageDtoSchema):
    fields: list
    __schema__ = RequestPatchMessageDtoSchema

    def __init__(self, *args, **kwargs):
        self.fields = []
        super(RequestPatchMessageDto, self).__init__(*args, **kwargs)

    def set(self, key, value):
        self.fields.append(key)
        super(RequestPatchMessageDto, self).set(key, value)


class RequestDeleteMessageDtoSchema(Schema):
    pass


class RequestDeleteMessageDto(RequestDto, RequestDeleteMessageDtoSchema):
    __schema__ = RequestDeleteMessageDtoSchema
