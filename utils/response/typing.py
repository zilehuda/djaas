from mypy_extensions import TypedDict


class DjaasApiResponse(TypedDict):
    success: bool
    message: str
    data: dict
    error: dict
