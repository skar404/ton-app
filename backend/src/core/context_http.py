from aio_clients import Http
from aio_clients import Options
from aio_clients.struct import Middleware

from core.logger import log


class HttpContext:
    _http_session: dict[str, Http] = dict()

    async def close_http_session(self) -> None:
        log.info(f"Close http sessions {list(self._http_session.keys())}")
        for name, http in self._http_session.items():
            await http.close()
            log.info(f"Http session closed {name}")

    def get_session(
            self,
            key: str,
            *,
            host: str = "",
            headers: dict[str, str] = None,
            option: Options | None = None,
            middleware: Middleware | None = None,
    ) -> Http:
        if not self._http_session.get(key):
            self._http_session[key] = Http(
                host=host,
                headers=headers,
                option=option,
                middleware=middleware,
            )
        return self._http_session[key]


http_ctx = HttpContext()
