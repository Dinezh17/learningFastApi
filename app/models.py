from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)         # specify a length
    author = Column(String(100), index=True)         # specify a length
    publishing_year = Column(Integer)
