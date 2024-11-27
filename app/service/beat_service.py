from sqlalchemy.orm import Session
from app.data import models, schemas
from app.repository.beat_repo import BeatRepository

beat_repo = BeatRepository()

class BeatService:
    def create_beat(self, beatsheet_id: int, beat: schemas.BeatCreate, db: Session):
        new_beat = models.Beat(
            description=beat.description,
            beatsheet_id=beatsheet_id)
        return beat_repo.create(new_beat, db)

    def get_beat(self, id: int, db: Session):
        return beat_repo.get_by_id(
            models.Beat,
            models.Beat.id,
            id,
            db)

    def update_beat(self,
                         curr_beat: models.Beat,
                         beat: schemas.BeatCreate,
                         db: Session):
        curr_beat.description = beat.description
        curr_beat.timestamp = beat.timestamp
        return beat_repo.update(curr_beat, db)

    def delete_beat(self,
                         curr_beat: models.Beat,
                         db: Session):
        return beat_repo.delete(curr_beat, db)

    def get_all_beat(self, db: Session):
        return beat_repo.get_all(models.Beat, db)

