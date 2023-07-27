from enum import IntEnum


class ReindexPageResponse500DataCode(IntEnum):
    VALUE_400 = 400
    VALUE_401 = 401
    VALUE_403 = 403
    VALUE_404 = 404
    VALUE_500 = 500
    VALUE_503 = 503

    def __str__(self) -> str:
        return str(self.value)
