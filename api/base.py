from marshmallow import ValidationError, Schema, EXCLUDE

from api.exceptions import ApiValidationException, ApiResponseValidationException


class RequestDto:
    __schema__: Schema

    def __init__(self, data: dict):
        try:
            valid_data = self.__schema__(unknown=EXCLUDE).load(data)
        except ValidationError as error:
            raise ApiValidationException(error.messages)
        else:
            self._import(valid_data)

    def _import(self, data: dict):
        for name, field in data.items():
            self.set(name, field)

    def set(self, key, value):
        setattr(self, key, value)


class ResponseDto:
    __schema__: Schema

    def __init__(self, obj: object, many: bool = False):
        # properties = {}
        # for prop in dir(obj):
        #     if not prop.startswith('_') and not prop.endswith('_'):
        #         attr = getattr(obj, prop)
        #         if not callable(attr):
        #             valid_data['prop'] = attr
        if many:
            properties = [self.parse_obj(o) for o in obj]
        else:
            properties = self.parse_obj(obj)

        # properties = {
        #     prop: value
        #     for prop in dir(obj)
        #     if not prop.startswith('_')
        #     and not prop.endswith('_')
        #     and not callable(value := getattr(obj, prop))
        # }

        # if type(obj) == list:
        #     for obj_of_list in list(obj):
        #         for prop in dir(obj_of_list):
        #             if not prop.startswith('_') and not prop.endswith('_'):
        #                 attr = getattr(obj_of_list, prop)
        #                 if not callable(attr):
        #                     if prop in properties:
        #                         properties[prop].append(attr)
        #                     else:
        #                         properties[prop] = [attr]

        try:
            self._data = self.__schema__(unknown=EXCLUDE, many=many).load(properties)
        except ValidationError as error:
            raise ApiResponseValidationException(error.messages)

    @staticmethod
    def parse_obj(obj: object) -> dict:
        return {
            prop: value
            for prop in dir(obj)
            if not prop.startswith('_')
               and not prop.endswith('_')
               and not callable(value := getattr(obj, prop))
        }

    def dump(self) -> dict:
        return self._data
