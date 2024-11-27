from sqlalchemy.orm import Session
from app.data import models, schemas
from app.repository.act_repo import ActRepository

act_repo = ActRepository()

class ActService:
    @staticmethod
    def create_act(beat_id: int, act: schemas.ActCreate, db: Session):
        new_act = models.Act(
            description=act.description,
            timestamp=act.timestamp,
            duration=act.duration,
            camera_angle=act.camera_angle,
            beat_id=beat_id)
        return act_repo.create(new_act, db)

    @staticmethod
    def get_act(id: int, db: Session):
        return act_repo.get_by_id(
            models.Act,
            models.Act.id,
            id,
            db)

    @staticmethod
    def update_act(curr_act: models.Act,
                   act: schemas.ActCreate,
                   db: Session):
        curr_act.description = act.description
        curr_act.timestamp = act.timestamp
        curr_act.duration = act.duration
        curr_act.camera_angle = act.camera_angle

        return act_repo.update(curr_act, db)

    @staticmethod
    def delete_act(curr_act: models.Act,
                   db: Session):
        return act_repo.delete(curr_act, db)

    @staticmethod
    def get_acts(db: Session):
        return act_repo.get_all(models.Act, db)

