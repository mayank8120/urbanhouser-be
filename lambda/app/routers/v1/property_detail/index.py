import os
import uuid

from fastapi import Depends, APIRouter, Form, UploadFile
from sqlalchemy.orm import Session

from app.models.db.property import Property
from app.models.db.property_images import PropertyImage
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
        # furnished: bool = Form(...),
        price: float = Form(...),
        state: str = Form(...),
        property_type: str = Form(...),
        furnishing_status: str = Form(...),
        balconies: int = Form(...),
        pincode: str = Form(...)
        , db: Session = Depends(get_db)):
    property_detail = {
        'user_id': user_id,
        'title': title,
        'description': description,
        'city': city,
        'address': address,
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'price': price,
        'state': state,
        'property_type': property_type,
        'furnishing_status': furnishing_status,
        'balconies': balconies,
        'pincode': pincode,
    }

    property_detail = Property(**property_detail)

    db.add(property_detail)
    db.commit()
    db.refresh(property_detail)

    image = images
    file_extension = os.path.splitext(image.filename)[1]
    secure_filename = f"{uuid.uuid4()}{file_extension}"

    images_dir = os.path.join(os.getcwd(), "images")
    os.makedirs(images_dir, exist_ok=True)

    image_path = os.path.join(images_dir, secure_filename)
    with open(image_path, "wb") as f:
        f.write(await image.read())

    new_image = PropertyImage(
        property_id=property_detail.id,
        image_url=image_path,
        is_main_image=True,
        # created_at=datetime.datetime.utcnow(),
        # updated_at=datetime.datetime.utcnow()
    )

    db.add(new_image)
    db.commit()

    return {"message": "User created successfully!", "user_id": property_detail.id}


@router.get("/{property_id}")
async def get_property(property_id: int, db: Session = Depends(get_db)):
    property = db.query(Property).filter(Property.id == property_id).first()
    images = db.query(PropertyImage).filter(PropertyImage.property_id == property_id).all()

    property.imagess = images

    if not property:
        return {"message": "Property not found"}, 404
    # Process or format property data if needed
    return property
