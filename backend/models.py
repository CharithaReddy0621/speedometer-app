from sqlalchemy import Column, Integer, Float
from database import Base

class SpeedData(Base):
    __tablename__ = 'speed_data'
    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer)
    speed = Column(Float)
