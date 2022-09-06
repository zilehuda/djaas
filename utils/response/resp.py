from utils.response.typing import DjaasApiResponse

""" # noqa
from rest_framework.response import Response

# 1 Response take get_response function
# 2 Status code by default is 200 and if you want to use other status codes than you can pass other status code as well

return Response(
                DjaasResponse.get_response(
                success=True,
                message="Any message",
                data={},
                error={},
                ),
                status_code
            )

"""


class DjaasResponse:
    @staticmethod
    def get_response(
        success: bool = False,
        is_validation_error: bool = False,
        message: str = "",
        code: int = 0,
        data: dict = None,
        error: dict = None,
        is_paginated: bool = False,
        pagination_data: dict = None,
    ) -> DjaasApiResponse:
        data = {} if data is None else data
        error = {} if error is None else error
        pagination_data = {} if pagination_data is None else pagination_data
        return {
            "success": success,
            "is_validation_error": is_validation_error,
            "message": message,
            "code": code,
            "data": data,
            "error": error,
            "is_paginated": is_paginated,
            "pagination": pagination_data,
        }
