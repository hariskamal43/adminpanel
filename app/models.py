from sqlalchemy import ForeignKey,Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable= False)
    username = Column(String, nullable= False, unique=True)
    email = Column(String,nullable=False ,unique=True)
    password = Column(String, nullable=False)

