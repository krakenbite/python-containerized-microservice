from fastapi import APIRouter
from containerized_microservice.api.v1 import router as api_v1_router
from containerized_microservice.api import health

router = APIRouter()
router.include_router(api_v1_router.router)
router.include_router(health.router)
