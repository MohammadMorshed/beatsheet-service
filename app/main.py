from fastapi import FastAPI
from app.api import beatsheet_api, beat_api, act_api
from app.data.database import engine, Base

# Initialize the database
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="BeatSheetService API",
    version="1.0",
    description="API for managing BeatSheets, Beats, and Acts",
)

# Include Routers
app.include_router(
    beatsheet_api.endpoints,
    prefix="/beatsheet",
    tags=["BeatSheets"])

app.include_router(
    beat_api.endpoints,
    prefix="/beatsheet/{beatsheet_id}/beat",
    tags=["Beats"])

app.include_router(
    act_api.endpoints,
    prefix="/beatsheet/{beatsheet_id}/beat/{beat_id}/act",
    tags=["Acts"])
