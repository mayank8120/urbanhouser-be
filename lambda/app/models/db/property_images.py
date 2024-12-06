from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.db.property import Property
from . import Base


class PropertyImage(Base):
    __tablename__ = 'property_images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    property_id = Column(Integer, ForeignKey('properties.id'), nullable=False)
    image_url = Column(String(255), nullable=False)
    is_main_image = Column(Boolean, default=False)
    # created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationship with Property model
    property = relationship(Property, backref="property_images")

    def __init__(self, property_id, image_url, is_main_image):
        self.property_id = property_id
        self.image_url = image_url
        self.is_main_image = is_main_image
        # self.created_at = created_at
        # self.updated_at = updated_at
