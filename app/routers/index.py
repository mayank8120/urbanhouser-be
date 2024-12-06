from fastapi import APIRouter

from app.routers.v1.auth.index import router as auth_r
from app.routers.v1.property_detail.index import router as property_d
from app.routers.v1.property_list.index import router as properties_d
from app.routers.v1.search_list.index import router as search_list
from app.routers.v1.test.index import router as img_route


#Router class is the class which is basically used to decleare the controllers
main_router = APIRouter()
main_router.include_router(auth_r)
main_router.include_router(img_route)
main_router.include_router(property_d)
main_router.include_router(properties_d)
main_router.include_router(search_list)

