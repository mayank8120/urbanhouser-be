from fastapi import APIRouter
from sqlalchemy import and_

from app.models.db import PropertyImage
from app.models.db.property import Property
from app.utils.database import get_db

router = APIRouter(
    prefix="/properties",
    tags=["Properties"],
)


@router.get("/")
async def get_properties(city: str, state: str):
    db = get_db()

    properties = db.query(Property).filter(
        and_
        (Property.city == city,
         Property.state == state)
    ).all()

    for property in properties:
        images = db.query(PropertyImage).filter(PropertyImage.property_id == property.id).all()
        property.images = images

    if not properties:
        return {"message": "Properties not found"}, 404

    return properties
