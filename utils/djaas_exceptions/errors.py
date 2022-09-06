from enum import Enum


class BaseErrorEnum(Enum):
    def __init__(self, error):
        self.error_code = error[0]
        self.error_message = error[1]

    @property
    def code(self):
        return self.error_code

    @property
    def message(self):
        return self.error_message


class DjaasError(BaseErrorEnum):
    SOMETHING_WENT_WRONG = (
        (1000, "Something went wrong. Please contact to Administrator"),
    )
    INVALID_CREDENTIALS = ((1001, "Invalid Credentials. Please try again"),)
    INVALID_TOKEN = ((1002, "Invalid Token"),)
    AUTH_TOKEN_EXPIRED = ((1003, "Auth Token has been Expired"),)


class DjaasResourceNotFoundError(BaseErrorEnum):
    RESOURCE_NOT_FOUND = ((2000, "Resource Not Found"),)


class DjaasValidationError(BaseErrorEnum):
    VALIDATION_ERROR = ((3000, "Validation Error"),)


class DjaasAuthorizedError(BaseErrorEnum):
    UNAUTHORIZED_ERROR = ((4000, "User is not authorized to perform this action"),)
