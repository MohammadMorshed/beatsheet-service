from sqlalchemy.orm import Session
from app.data import models, schemas
from app.repository.beatsheet_repo import BeatsheetRepository

beatsheet_repo = BeatsheetRepository()

class BeatsheetService:
    def create_beatsheet(self, beatsheet: schemas.BeatSheetCreate, db: Session):
        beatsheet = models.BeatSheet(title=beatsheet.title)
        return beatsheet_repo.create(beatsheet, db)

    def get_beatsheet(self, id: int, db: Session):
        return beatsheet_repo.get_by_id(
            models.BeatSheet,
            models.BeatSheet.id,
            id,
            db)

    def update_beatsheet(self,
                         curr_beatsheet: models.BeatSheet,
                         beatsheet: schemas.BeatSheetCreate,
                         db: Session):
        curr_beatsheet.title = beatsheet.title
        return beatsheet_repo.update(curr_beatsheet, db)

    def delete_beatsheet(self,
                         curr_beatsheet: models.BeatSheet,
                         db: Session):
        return beatsheet_repo.delete(curr_beatsheet, db)

    def get_all_beatsheets(self, db: Session):
        return beatsheet_repo.get_all(models.BeatSheet, db)

