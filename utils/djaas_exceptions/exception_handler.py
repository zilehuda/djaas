import traceback

from rest_framework.response import Response
from rest_framework.views import exception_handler

from utils.response.resp import DjaasResponse
from .errors import (
    DjaasAuthorizedError,
    DjaasError,
    DjaasResourceNotFoundError,
    DjaasValidationError,
)
from .exceptions import DjaasBaseException, DjaasValidationException
from django.conf import settings


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__
    print("exception_class: ", exception_class)
    handlers = {
        # Rest Framework Exceptions
        "ValidationError": _handle_validation_error,
        "Http404": _handle_not_found_error,
        "PermissionDenied": _handle_authenticated_error,
        "NotAuthenticated": _handle_authenticated_error,
        "InvalidToken": _handle_invalid_token_error,
        "AuthenticationFailed": _handle_invalid_cred_error,
        # Other Exceptions
        "TokenError": _handle_token_error,
        "KeyError": _handle_key_error,
        "DoesNotExist": _handle_resource_does_not_exist_error,
    }

    if isinstance(exc, DjaasBaseException):
        return _handle_base_exceptions(exc, context, response)
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return _handle_unexpected_error(exc, context, response)


# Rest Exception Handlers


def _handle_unexpected_error(exc, context, response):
    traceback.print_exc()
    # capture_exception(exc)

    res = DjaasResponse.get_response(
        success=False,
        code=DjaasError.SOMETHING_WENT_WRONG.code,
        message=DjaasError.SOMETHING_WENT_WRONG.message,
    )
    if response is None:
        return Response(res, status=500)

    response.data = res
    return response


def _handle_not_found_error(exc, context, response):
    response.data = DjaasResponse.get_response(
        success=False,
        code=DjaasResourceNotFoundError.RESOURCE_NOT_FOUND.code,
        message=DjaasResourceNotFoundError.RESOURCE_NOT_FOUND.message,
    )
    return response


def _handle_authenticated_error(exc, context, response):
    response.data = DjaasResponse.get_response(
        success=False,
        code=DjaasAuthorizedError.UNAUTHORIZED_ERROR.code,
        message=DjaasAuthorizedError.UNAUTHORIZED_ERROR.message,
    )
    return response


def _handle_invalid_token_error(exc, context, response):
    response.data = DjaasResponse.get_response(
        success=False,
        code=DjaasError.INVALID_TOKEN.code,
        message=DjaasError.INVALID_TOKEN.message,
    )
    return response


def _handle_invalid_cred_error(exc, context, response):
    response.data = DjaasResponse.get_response(
        success=False,
        code=DjaasError.INVALID_CREDENTIALS.code,
        message=DjaasError.INVALID_CREDENTIALS.message,
    )
    return response


def _handle_validation_error(exc, context, response):
    response.data = DjaasResponse.get_response(
        success=False,
        error=exc.detail,
        code=DjaasValidationError.VALIDATION_ERROR.code,
        message=DjaasValidationError.VALIDATION_ERROR.message,
        is_validation_error=True,
    )
    return response


def _handle_base_exceptions(exc, context, response):
    if isinstance(exc, DjaasValidationException):
        response.data = DjaasResponse.get_response(
            success=False,
            error=exc.error,
            code=DjaasValidationError.VALIDATION_ERROR.code,
            message=DjaasValidationError.VALIDATION_ERROR.message,
            is_validation_error=True,
        )
    else:
        response.data = DjaasResponse.get_response(
            success=False,
            code=exc.error.code,
            message=exc.error.message.format(value=exc.value),
        )
    return response


# Other Handlers


def _handle_token_error(exc, context, response):
    return Response(
        DjaasResponse.get_response(
            success=False,
            code=DjaasError.INVALID_TOKEN.code,
            message=DjaasError.INVALID_TOKEN.message,
        ),
        status=400,
    )


def _handle_resource_does_not_exist_error(exc, context, response):
    return Response(
        DjaasResponse.get_response(
            success=False,
            code=DjaasResourceNotFoundError.RESOURCE_NOT_FOUND.code,
            message=DjaasResourceNotFoundError.RESOURCE_NOT_FOUND.message,
        ),
        status=404,
    )


def _handle_key_error(exc, context, response):
    return Response(
        DjaasResponse.get_response(
            success=False,
            code=DjaasValidationError.VALIDATION_ERROR.code,
            message=DjaasValidationError.VALIDATION_ERROR.message,
            error={exc.args[0]: [exc.args[0] + " is invalid"]},
        ),
        status=400,
    )
