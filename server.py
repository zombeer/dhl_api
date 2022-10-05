import json

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi_cache import caches, close_caches
from fastapi_cache.backends.redis import CACHE_KEY, RedisCacheBackend

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


def redis_cache():
    return caches.get(CACHE_KEY)


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
async def track_shipping(
    payload: TrackingNumber = Depends(),
    cache: RedisCacheBackend = Depends(redis_cache),
):
    """
    Primary function. Track shipping by its number.
    """
    in_cache = await cache.get(payload.num)
    if in_cache:
        return json.loads(in_cache)

    result = get_tracking_data(payload.num)
    if result.status_code == 200:
        await cache.set(payload.num, result.text)
    return result.json()


@app.on_event("startup")
async def on_startup() -> None:
    """
    Some preparation.
    """
    rc = RedisCacheBackend(REDIS_URL)
    caches.set(CACHE_KEY, rc)


@app.on_event("shutdown")
async def on_shutdown() -> None:
    """
    Teardown.
    """
    await close_caches()
