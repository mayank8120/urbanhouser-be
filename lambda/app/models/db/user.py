from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    properties = relationship('Property', back_populates="user")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
