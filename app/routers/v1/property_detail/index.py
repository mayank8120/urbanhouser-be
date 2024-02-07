import datetime

from fastapi import Depends, APIRouter, Form, UploadFile
from sqlalchemy.orm import Session

from app.models.db.user import User
from app.utils.database import get_db

router = APIRouter(
    prefix="/property",
    tags=["Property"],
)


@router.post("/")
async def post_property(
        images: UploadFile = Form(...),
        user_id: int = Form(...),
        title: str = Form(...),
        description: str = Form(...),
        city: str = Form(...),
        address: str = Form(...),
        area: float = Form(...),
        bedrooms: int = Form(...),
        bathrooms: int = Form(...),
        furnished: bool = Form(...),
        price: float = Form(...),
        state: str = Form(...),
        property_type: str = Form(...),
        furnishing_status: str = Form(...),
        balconies: int = Form(...),
        pincode: str = Form(...),
        availability_date: datetime = Form(...),
        created_at: datetime = Form(...),
        updated_at: datetime = Form(...)
        , db: Session = Depends(get_db)):










    user = User(**user.dict())

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User created successfully!", "user_id": user.id}
