from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.data import schemas, database
from app.service.beatsheet_service import BeatsheetService

endpoints = APIRouter()
service = BeatsheetService()

# Route to create a new BeatSheet
@endpoints.post("/", response_model=schemas.BeatSheet)
def create_beatsheet(beatsheet: schemas.BeatSheetCreate, db: Session = Depends(database.get_db)):
    return service.create_beatsheet(beatsheet, db)


# Route to get a BeatSheet by ID
@endpoints.get("/{id}", response_model=schemas.BeatSheet)
def get_beatsheet(id: int, db: Session = Depends(database.get_db)):
    curr_beatsheet = service.get_beatsheet(id, db)
    if curr_beatsheet is None:
        raise HTTPException(status_code=404, detail="BeatSheet not found")
    return curr_beatsheet


# Route to update a BeatSheet by ID
@endpoints.put("/{id}", response_model=schemas.BeatSheet)
def update_beatsheet(id: int, beatsheet: schemas.BeatSheetCreate, db: Session = Depends(database.get_db)):
    curr_beatsheet = service.get_beatsheet(id, db)
    if curr_beatsheet is None:
        raise HTTPException(status_code=404, detail="BeatSheet not found")
    return service.update_beatsheet(curr_beatsheet, beatsheet, db)


# Route to delete a BeatSheet by ID
@endpoints.delete("/{id}")
def delete_beatsheet(id: int, db: Session = Depends(database.get_db)):
    curr_beatsheet = service.get_beatsheet(id, db)
    if curr_beatsheet is None:
        raise HTTPException(status_code=404, detail="BeatSheet not found")
    service.delete_beatsheet(curr_beatsheet, db)
    return {"message": f"Beatsheet with ID {id} deleted successfully"}


# Route to list all BeatSheets
@endpoints.get("/", response_model=List[schemas.BeatSheet])
def get_all_beatsheets(db: Session = Depends(database.get_db)):
    return service.get_all_beatsheets(db)
