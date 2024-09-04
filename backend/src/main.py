import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import clients
from clients.stonfi import StonFi, StonFiEx
from core.context_http import http_ctx
from core.logger import log
from core.cache import ctx_cache
import api
from core.settings import env


async def update_cache():
    try:
        ctx_cache['tsTON'] = (await clients.StonFi().get_token_info(
            clients.TokenAddress.tsTON
        )).json
        ctx_cache['TON'] = (await StonFi().get_token_info(
            clients.TokenAddress.TON
        )).json
    except StonFiEx as ex:
        log.error('Error while updating cache %s', ex)
        return

    log.info('Cache updated')


async def while_update_cache():
    while True:
        await asyncio.sleep(env.cache_time)
        try:
            await update_cache()
        except Exception as ex:
            log.exception('Error while updating cache ex=%s', ex)


async def startup_event():
    try:
        await update_cache()
    except Exception as ex:
        log.exception('Error while updating cache ex=%s', ex)
    task = asyncio.create_task(while_update_cache())
    task.add_done_callback(lambda _: log.info("Update_cache Task done"))
    app.ctx_task = task


async def shutdown_event():
    app.ctx_task.cancel()
    await http_ctx.close_http_session()
    log.info('Shutdown')


app = FastAPI(
    on_startup=[startup_event],
    on_shutdown=[shutdown_event],

)

origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.public_router)
