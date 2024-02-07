import os
import uuid

from fastapi import APIRouter, Form, Depends, UploadFile
from sqlalchemy.orm import Session

from app.models.db.test import ImageTable
from app.utils.database import get_db

router = APIRouter(
    prefix="/test",
    tags=["Auth"],
)


@router.post("/upload")
async def upload_image(txt: str = Form(...),
                       image_url: UploadFile = Form(...),
                       db: Session = Depends(get_db)):
    image = image_url
    file_extension = os.path.splitext(image.filename)[1]
    secure_filename = f"{uuid.uuid4()}{file_extension}"

    images_dir = os.path.join(os.getcwd(), "images")
    os.makedirs(images_dir, exist_ok=True)

    image_path = os.path.join(images_dir, secure_filename)
    with open(image_path, "wb") as f:
        f.write(await image.read())

    new_image = ImageTable(txt=txt, image_url=secure_filename)  # Store relative path

    # Add the image to the database
    db.add(new_image)
    db.commit()

    db.refresh(new_image)
    return {"message": "Image uploaded successfully"}
