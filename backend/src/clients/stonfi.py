import enum

from aio_clients.struct import Middleware

from core.context_http import http_ctx
from core.exceptions import BackendEx
from core.logger import log


class TokenAddress(enum.StrEnum):
    tsTON = "0:bdf3fa8098d129b54b4f73b5bac5d1e1fd91eb054169c3916dfc8ccd536d1000"
    TON = "0:0000000000000000000000000000000000000000000000000000000000000000"


class StonFiEx(BackendEx):
    pass


class StonFi:
    def __init__(self):
        self.api = http_ctx.get_session(
            self.__class__,
            host="https://api.ston.fi/v1/assets/",
            headers={
                "Content-Type": "application/json",
            },
            middleware=Middleware(
                end=[
                    self.middleware_check_data,
                ],
            ),
        )

    @staticmethod
    async def middleware_check_data(response, **kwargs):
        if response.code > 299:
            log.error(f"stonFi middleware_check_data error: f{response.json}")
            raise StonFiEx()

    def get_token_info(self, token_address: TokenAddress):
        return self.api.get(str(token_address.value))
