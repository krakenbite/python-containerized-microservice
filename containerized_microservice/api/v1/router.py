from fastapi import APIRouter
from containerized_microservice.api.v1 import target

router = APIRouter(prefix="/v1")
router.include_router(target.router)
