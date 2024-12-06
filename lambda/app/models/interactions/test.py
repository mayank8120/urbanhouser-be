from fastapi import UploadFile
from pydantic import BaseModel


# class CreateTest(BaseModel):
#     file: UploadFile = File(...))
#     image_url: str
#     txt: str
#


class UploadRequestss(BaseModel):
    title: str
    image: UploadFile
