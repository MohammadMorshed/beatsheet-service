from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.data.database import Base
from datetime import datetime

class BeatSheet(Base):
    __tablename__ = "beatsheets"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    beats = relationship("Beat", back_populates="beatsheet", cascade="all, delete")

class Beat(Base):
    __tablename__ = "beats"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    beatsheet_id = Column(Integer, ForeignKey("beatsheets.id"))
    acts = relationship("Act", back_populates="beat", cascade="all, delete")
    beatsheet = relationship("BeatSheet", back_populates="beats")

class Act(Base):
    __tablename__ = "acts"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    duration = Column(Integer)
    camera_angle = Column(String)
    beat_id = Column(Integer, ForeignKey("beats.id"))
    beat = relationship("Beat", back_populates="acts")
