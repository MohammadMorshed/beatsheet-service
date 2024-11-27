from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.data import schemas
from app.data.database import get_db
from typing import List
from app.service.beatsheet_service import BeatsheetService
from app.service.beat_service import BeatService

endpoints = APIRouter()
beat_service = BeatService()
beatsheet_service = BeatsheetService()


@endpoints.get("/", response_model=List[schemas.Beat])
def get_beats(beatsheet_id: int, db: Session = Depends(get_db)):
    """Retrieve all beats."""
    return beat_service.get_all_beat(db)


@endpoints.get("/{beat_id}", response_model=schemas.Beat)
def get_beat(beatsheet_id: int, beat_id: int, db: Session = Depends(get_db)):
    """Retrieve a single beat by ID."""
    beat = beat_service.get_beat(beat_id, db)
    if not beat:
        raise HTTPException(status_code=404, detail="Beat not found")
    return beat


@endpoints.post("/", response_model=schemas.Beat)
def create_beat(beatsheet_id: int, beat: schemas.BeatCreate, db: Session = Depends(get_db)):
    """Create a new beat associated with a BeatSheet."""
    beatsheet = beatsheet_service.get_beatsheet(beatsheet_id, db)
    if not beatsheet:
        raise HTTPException(status_code=404, detail="BeatSheet not found")

    beat = beat_service.create_beat(beatsheet.id, beat, db)
    return beat


@endpoints.put("/{beat_id}", response_model=schemas.Beat)
def update_beat(beatsheet_id: int, beat_id: int, beat: schemas.BeatCreate, db: Session = Depends(get_db)):
    """Update an existing beat."""
    curr_beat = beat_service.get_beat(beat_id, db)
    if not curr_beat:
        raise HTTPException(status_code=404, detail="Beat not found")
    updated_beat = beat_service.update_beat(curr_beat, beat, db)
    return updated_beat


@endpoints.delete("/{beat_id}")
def delete_beat(beatsheet_id: int, beat_id: int, db: Session = Depends(get_db)):
    """Delete a beat."""
    curr_beat = beat_service.get_beat(beat_id, db)
    if not curr_beat:
        raise HTTPException(status_code=404, detail="Beat not found")
    beat_service.delete_beat(curr_beat, db)
    return {"message": f"Beat with ID {beat_id} deleted successfully"}
