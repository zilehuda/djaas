from contextlib import contextmanager

from rest_framework.exceptions import APIException


@contextmanager
def does_not_raise():
    yield


class DjaasBaseException(APIException):
    pass


class DjaasException(DjaasBaseException):
    def __init__(self, error, value: str = ""):
        self.error = error
        self.value = value
        self.status_code = 400
        super().__init__(self.error, self.status_code)


class DjaasValidationException(DjaasBaseException):
    def __init__(self, error, value: str = ""):
        self.error = error
        self.value = value
        self.status_code = 400
        super().__init__(self.error, self.status_code)


class DjaasResourceNotFoundException(DjaasBaseException):
    def __init__(self, error, value: str = ""):
        self.error = error
        self.value = value
        self.status_code = 404
        super().__init__(self.error, self.status_code)


class DjaasResourceAlreadyExistException(DjaasBaseException):
    def __init__(self, error, value: str = ""):
        self.error = error
        self.value = value
        self.status_code = 409
        super().__init__(self.error, self.status_code)


class DjaasUnauthorizedException(DjaasBaseException):
    def __init__(self, error, value: str = ""):
        self.error = error
        self.value = value
        self.status_code = 403
        super().__init__(self.error, self.status_code)
