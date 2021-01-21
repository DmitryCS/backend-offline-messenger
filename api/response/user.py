from marshmallow import Schema, fields, pre_load, post_load

from api.base import ResponseDto


class ResponseCreateUserDtoSchema(Schema):
    id = fields.Int(required=True)
    login = fields.Str(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)

    @pre_load
    @post_load
    def serialize_datetime(self, data: dict, **kwargs) -> dict:
        if 'created_at' in data:
            data['created_at'] = str(data['created_at'])
        if 'updated_at' in data:
            data['updated_at'] = str(data['updated_at'])

        return data


class ResponseCreateUserDto(ResponseDto, ResponseCreateUserDtoSchema):
    __schema__ = ResponseCreateUserDtoSchema


class ResponseGetUserDtoSchema(Schema):
    login = fields.Str(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)

    @pre_load
    @post_load
    def serialize_datetime(self, data: dict, **kwargs) -> dict:
        if 'created_at' in data:
            data['created_at'] = str(data['created_at'])
        if 'updated_at' in data:
            data['updated_at'] = str(data['updated_at'])

        return data


class ResponseGetUserDto(ResponseDto, ResponseGetUserDtoSchema):
    __schema__ = ResponseGetUserDtoSchema


class ResponsePatchUserDtoSchema(Schema):
    id = fields.Int(required=True)
    login = fields.Str(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)

    @pre_load
    @post_load
    def serialize_datetime(self, data: dict, **kwargs) -> dict:
        if 'created_at' in data:
            data['created_at'] = str(data['created_at'])
        if 'updated_at' in data:
            data['updated_at'] = str(data['updated_at'])

        return data


class ResponsePatchUserDto(ResponseDto, ResponsePatchUserDtoSchema):
    __schema__ = ResponsePatchUserDtoSchema
