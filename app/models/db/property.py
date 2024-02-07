from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, Boolean, Text, DateTime, ForeignKey, relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    city = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    area = Column(Float, nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    furnished = Column(Boolean, nullable=False)
    price = Column(Float, nullable=False)
    state = Column(String(255), nullable=False)
    property_type = Column(String(255), nullable=False)
    furnishing_status = Column(String(255), nullable=False)
    balconies = Column(Integer, nullable=False)
    pincode = Column(String(255), nullable=False)
    availability_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", backref="properties")

    # Add other relationships if needed (e.g., with PropertyImage model)