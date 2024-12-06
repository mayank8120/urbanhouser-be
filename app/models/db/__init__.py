from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .property import *
from .user import *
from .property_images import *
