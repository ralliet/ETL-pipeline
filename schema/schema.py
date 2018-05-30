from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *
engine = create_engine('sqlite:///demo.db')

Base = declarative_base()
 
class Users(Base):
    __tablename__ = "users"
    UserId = Column(Integer, primary_key=True)
    Title = Column(String)
    FirstName = Column(String)
    LastName = Column(String)
    Email = Column(String)
    Username = Column(String)
    DOB = Column(DateTime)
class Uploads(Base):
    __tablename__ = "uploads"
    UploadId = Column(Integer, primary_key=True)
    UserId = Column(Integer)
    Title = Column(String)
    Body = Column(String)
    Timestamp = Column(DateTime)

#check if tables don't exist already
Users.__table__.create(bind=engine, checkfirst=True)
Uploads.__table__.create(bind=engine, checkfirst=True)