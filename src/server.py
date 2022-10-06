from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

from config import ENABLE_CORS, REDIS_URL, SELF_URL
from dhl import get_tracking_data
from response_class import PrettyJSONResponse
from schemas import TrackingNumber

BASE_URL = "https://api-eu.dhl.com/track/shipments"


app = FastAPI(
    title="DHL API Forwarding",
    description="Simple DHL track API...",
    contact={"email": "zombeer@gmail.com"},
    version="0.1.0",
    servers=[{"url": SELF_URL}],
)

if ENABLE_CORS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_headers=["*"],
        allow_methods=["*"],
        allow_credentials=True,
    )


@app.get("/", tags=["Info"], name="Redirect to API docs.")
def serve_main():
    """
    Redirect to API documentation page.
    """
    return RedirectResponse("/docs")


@app.get(
    "/track/",
    tags=["Track shipping"],
    name="Track shipping number.",
    response_class=PrettyJSONResponse,
)
@cache(expire=600)
async def track_shipping(payload: TrackingNumber = Depends()):
    """
    Primary function. Track shipping by its number.
    """
    result = get_tracking_data(payload.num)
    return result.json()


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(REDIS_URL, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
