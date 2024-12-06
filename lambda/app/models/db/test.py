from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ImageTable(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, unique=True, nullable=True)
    txt = Column(String, nullable=False)
