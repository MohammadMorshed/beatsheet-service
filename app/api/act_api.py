from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.data import models, schemas
from app.data.database import get_db
from typing import List

from app.service.next_act_predictor import next_act_predictor
from app.data.schemas import SuggestionRequest
from app.service.act_service import ActService
from app.service.beat_service import BeatService

endpoints = APIRouter()
act_service = ActService()
beat_service = BeatService()

@endpoints.get("/", response_model=List[schemas.Act])
def get_acts(beatsheet_id: int, beat_id: int, db: Session = Depends(get_db)):
    """Retrieve all acts."""
    return act_service.get_acts(db)


@endpoints.get("/{act_id}", response_model=schemas.Act)
def get_act(beatsheet_id: int, beat_id: int, act_id: int, db: Session = Depends(get_db)):
    """Retrieve a single act by ID."""
    act = act_service.get_act(act_id, db)
    if not act:
        raise HTTPException(status_code=404, detail="Act not found")
    return act


@endpoints.post("/", response_model=schemas.Act)
def create_act(beatsheet_id: int, beat_id: int, act: schemas.ActCreate, db: Session = Depends(get_db)):
    """Create a new act associated with a Beat."""
    beat = beat_service.get_beat(beat_id, db)
    if not beat:
        raise HTTPException(status_code=404, detail="Beat not found")

    return act_service.create_act(beat_id, act, db)


@endpoints.put("/{act_id}", response_model=schemas.Act)
def update_act(beatsheet_id: int, beat_id: int, act_id: int, act: schemas.ActCreate, db: Session = Depends(get_db)):
    """Update an existing act."""
    curr_act = act_service.get_act(act_id, db)
    if not curr_act:
        raise HTTPException(status_code=404, detail="Act not found")

    return act_service.update_act(curr_act, act, db)


@endpoints.delete("/{act_id}")
def delete_act(beatsheet_id: int, beat_id: int, act_id: int, db: Session = Depends(get_db)):
    """Delete an act."""
    curr_act = act_service.get_act(act_id, db)
    if not curr_act:
        raise HTTPException(status_code=404, detail="Act not found")

    act_service.delete_act(curr_act, db)
    return {"message": f"Act with ID {act_id} deleted successfully"}


@endpoints.post("/suggest-next")
def suggest_next(request: SuggestionRequest):
    suggestion = next_act_predictor.predict(request.current_act)
    return {"suggestion": suggestion}

@endpoints.post("/suggest")
def suggest_next(request: SuggestionRequest):
    suggestions = next_act_predictor.predict_sequence(request.current_act, request.count)
    return {"suggestions": suggestions}