from fastapi import APIRouter, Response
import http

router = APIRouter()


@router.get("/health")
async def health() -> Response:
    return Response(status_code=http.HTTPStatus.OK)
