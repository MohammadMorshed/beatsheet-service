from sqlalchemy.orm import Session
from app.data import models


class CrudRepository:
    @staticmethod
    def create(entity: any, db: Session):
        """
        Creates a new entity in the database.

        Args:
            entity (any): The entity to be created.
            db (Session): The database session.

        Returns:
            any: The created entity.
        """
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def update(entity: any, db: Session):
        """
        Updates an entity in the database.

        Args:
            entity (any): The entity to be updated.
            db (Session): The database session.

        Returns:
            any: The updated entity.
        """
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete(entity: any, db: Session):
        """
        Deletes an entity from the database.

        Args:
            entity (any): The entity to be deleted.
            db (Session): The database session.

        Returns:
            any: The deleted entity.
        """
        db.delete(entity)
        db.commit()
        return entity

    @staticmethod
    def get_by_id(entity: any, entity_id_field: any, id: any, db: Session):
        """
        Retrieves an entity by its ID from the database.

        Args:
            entity (any): The entity class to query.
            entity_id_field (any): The field representing the entity's ID.
            id (any): The ID of the entity to retrieve.
            db (Session): The database session.

        Returns:
            any: The entity with the specified ID, or None if not found.
        """
        return db.query(entity).filter(entity_id_field == id).first()

    @staticmethod
    def get_all(entity: any, db: Session):
        """
        Retrieves all entities of the given type from the database.

        Args:
            entity (any): The entity class to query.
            db (Session): The database session.

        Returns:
            list: All entities of the given type.
        """
        return db.query(entity).all()