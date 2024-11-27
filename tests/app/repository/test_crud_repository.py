from unittest.mock import MagicMock

import pytest
from sqlalchemy.exc import IntegrityError

from app.repository.crud_repo import CrudRepository

# Set up the CrudRepository instance for testing
crud_repo = CrudRepository()


def test_create():
    """Test the create method."""
    # mocks
    mock_db = MagicMock()
    mock_entity = MagicMock()

    result = crud_repo.create(mock_entity, mock_db)

    # verify
    mock_db.add.assert_called_once_with(mock_entity)
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(mock_entity)

    assert result == mock_entity


def test_create_failure():
    """Test the create method when db.add or db.commit fails."""
    # mocks
    mock_db = MagicMock()
    mock_db.commit.side_effect = IntegrityError("Integrity error", None, None)
    mock_entity = MagicMock()

    with pytest.raises(IntegrityError):
        crud_repo.create(mock_entity, mock_db)

    # verify
    mock_db.add.assert_called_once_with(mock_entity)
    mock_db.commit.assert_called_once()


def test_update():
    """Test the update method."""
    # mocks
    mock_db = MagicMock()
    mock_entity = MagicMock()

    result = crud_repo.update(mock_entity, mock_db)

    # verify
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(mock_entity)

    assert result == mock_entity


def test_update_failure():
    """Test the update method when db.commit fails."""
    # mocks
    mock_db = MagicMock()
    mock_db.commit.side_effect = IntegrityError("Integrity error", None, None)

    mock_entity = MagicMock()

    with pytest.raises(IntegrityError):
        crud_repo.update(mock_entity, mock_db)

    # verify
    mock_db.commit.assert_called_once()


def test_delete():
    """Test the delete method."""
    # mocks
    mock_db = MagicMock()
    mock_entity = MagicMock()

    result = crud_repo.delete(mock_entity, mock_db)

    # verify
    mock_db.delete.assert_called_once_with(mock_entity)
    mock_db.commit.assert_called_once()

    assert result == mock_entity


def test_delete_failure():
    """Test the delete method when db.commit fails."""
    # mocks
    mock_db = MagicMock()
    mock_db.commit.side_effect = IntegrityError("Integrity error", None, None)

    mock_entity = MagicMock()

    with pytest.raises(IntegrityError):
        crud_repo.delete(mock_entity, mock_db)

    # verify
    mock_db.delete.assert_called_once_with(mock_entity)
    mock_db.commit.assert_called_once()


def test_get_by_id():
    """Test the get_by_id method."""
    # mocks
    mock_db = MagicMock()
    mock_entity = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = mock_entity

    result = crud_repo.get_by_id(MagicMock, MagicMock, 1, mock_db)

    # verify
    mock_db.query.assert_called_once()
    mock_db.query.return_value.filter.assert_called_once()
    mock_db.query.return_value.filter.return_value.first.assert_called_once()

    assert result == mock_entity


def test_get_by_id_not_found():
    """Test the get_by_id method when the entity is not found."""
    # mocks
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = None

    result = crud_repo.get_by_id(MagicMock, MagicMock, 999, mock_db)

    # verify
    mock_db.query.assert_called_once()
    mock_db.query.return_value.filter.assert_called_once()
    mock_db.query.return_value.filter.return_value.first.assert_called_once()

    assert result is None


def test_get_all():
    """Test the get_all method."""
    # mocks
    mock_db = MagicMock()
    mock_entities = [MagicMock(), MagicMock()]

    mock_db.query.return_value.all.return_value = mock_entities

    result = crud_repo.get_all(MagicMock, mock_db)

    # verify
    mock_db.query.assert_called_once()
    mock_db.query.return_value.all.assert_called_once()

    assert result == mock_entities


def test_get_all_empty():
    """Test the get_all method when no entities exist."""
    # mocks
    mock_db = MagicMock()
    mock_db.query.return_value.all.return_value = []

    result = crud_repo.get_all(MagicMock, mock_db)

    # verify
    mock_db.query.assert_called_once()
    mock_db.query.return_value.all.assert_called_once()

    assert result == []
