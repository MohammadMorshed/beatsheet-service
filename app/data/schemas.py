from dataclasses import field

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ActBase(BaseModel):
    description: str
    timestamp: Optional[datetime] = datetime.utcnow()
    duration: Optional[int]
    camera_angle: Optional[str]

class ActCreate(ActBase):
    pass

class Act(ActBase):
    id: int
    class Config:
        from_attributes = True

class BeatBase(BaseModel):
    description: str
    timestamp: Optional[datetime] = datetime.utcnow()

class BeatCreate(BeatBase):
    pass

class Beat(BeatBase):
    id: int
    acts: List[Act] = field(default_factory=list)
    class Config:
        from_attributes = True

class BeatSheetBase(BaseModel):
    title: str

class BeatSheetCreate(BeatSheetBase):
    pass

class BeatSheet(BeatSheetBase):
    id: int
    beats: List[Beat] = field(default_factory=list)
    class Config:
        from_attributes = True

class SuggestionRequest(BaseModel):
    current_act: str
    count: int = 1
