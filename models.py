from sqlalchemy import Integer, String, Column
from database import Base

class Books(Base):
    __tablename__ = "books"  # This is the table inside the database 'fastapidb'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    rating = Column(Integer)
