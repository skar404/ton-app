from decimal import Decimal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core.cache import ctx_cache

public_router = APIRouter()


class TokenInfoResponse(BaseModel):
    display_name: str
    symbol: str
    price_usd: Decimal


class ExchangeRateResponse(BaseModel):
    tsTON: TokenInfoResponse
    TON: TokenInfoResponse


@public_router.get("/exchange-rate")
async def get_data():
    if not ctx_cache:
        raise HTTPException(
            status_code=500,
            detail="Error api method"
        )

    TON = ctx_cache.get('TON').get('asset')
    tsTON = ctx_cache.get('tsTON').get('asset')

    return ExchangeRateResponse(
        tsTON=TokenInfoResponse(
            display_name=tsTON['display_name'],
            symbol='tsTON',
            price_usd=Decimal(tsTON['dex_usd_price'])
        ),
        TON=TokenInfoResponse(
            display_name=TON['display_name'],
            symbol='TON',
            price_usd=Decimal(TON['dex_usd_price'])
        )
    )
