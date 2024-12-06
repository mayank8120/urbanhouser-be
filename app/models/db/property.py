from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    city = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    area = Column(Float, nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    state = Column(String(255), nullable=False)
    property_type = Column(String(255), nullable=False)
    furnishing_status = Column(String(255), nullable=False)
    balconies = Column(Integer, nullable=False)
    pincode = Column(String(255), nullable=False)
    # availability_date = Column(DateTime)
    # created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship('User', backref="user_properties")  # Relationship defined correctly

    def __init__(self, user_id, title, description, city, address, area,
                 bedrooms, bathrooms, price, state, property_type,
                 furnishing_status, balconies, pincode):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.city = city
        self.address = address
        self.area = area
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.state = state
        self.property_type = property_type
        self.furnishing_status = furnishing_status
        self.balconies = balconies
        self.pincode = pincode
        # self.created_at = created_at
        # self.updated_at = updated_at
