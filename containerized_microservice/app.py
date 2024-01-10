from typing import AsyncIterator
from fastapi import FastAPI
from containerized_microservice.api import router
from contextlib import asynccontextmanager
import asyncio
import logging

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Lifecycle method to intercept FastAPI lifecycle."""
    try:
        logger.info("Starting up FastAPI Application...")
        yield
    except asyncio.exceptions.CancelledError:
        pass
    finally:
        logger.info("Shutting down FastAPI Application...")


app = FastAPI(title="Containerized Microservice", lifespan=lifespan)
app.include_router(router.router)
