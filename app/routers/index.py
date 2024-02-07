from fastapi import APIRouter

from app.routers.v1.auth.index import router as auth_r
from app.routers.v1.test.index import router as img_route

main_router = APIRouter()
main_router.include_router(auth_r)
main_router.include_router(img_route)
