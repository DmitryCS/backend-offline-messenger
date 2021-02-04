from sanic.exceptions import SanicException


class SanicRequestValidationException(SanicException):
    status_code = 400


class SanicUserConflictException(SanicException):
    status_code = 409


class SanicResponseValidationException(SanicException):
    status_code = 500


class SanicPasswordHashException(SanicException):
    status_code = 500


class SanicDBException(SanicException):
    status_code = 500


class SanicAuthException(SanicException):
    status_code = 401


class SanicUserNotFound(SanicException):
    status_code = 404


class SanicMessageNotFound(SanicException):
    status_code = 404


class SanicFileNotFound(SanicException):
    status_code = 404


class SanicMessageDeleted(SanicException):
    status_code = 404
