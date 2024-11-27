from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.api import beat_api
from app.data import schemas
from app.service.beat_service import BeatService
from app.service.beatsheet_service import BeatsheetService


def test_get_beat():
    """
    Test the get_beat method.

    Verifies that the get_beat method returns a beat by id.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 1
    beat = schemas.Beat(id=beat_id, description="Test Beat")

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_beat_service = MagicMock(spec=BeatService)
    beat_api.beat_service = mock_beat_service
    mock_beat_service.get_beat.return_value = beat

    # Act
    retrieved_beat = beat_api.get_beat(beatsheet_id, beat_id, mock_db)

    # Assert
    assert retrieved_beat == beat

    # verify
    mock_beat_service.get_beat.assert_called_once_with(beat_id, mock_db)


def test_get_beat_not_found():
    """
    Test the get_beat method with a non-existent id.

    Verifies that the get_beat method returns None when the beat is not found.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 999

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_beat_service = MagicMock(spec=BeatService)
    beat_api.beat_service = mock_beat_service
    mock_beat_service.get_beat.return_value = None

    # Act
    with pytest.raises(HTTPException) as e:
        beat_api.get_beat(beatsheet_id, beat_id, mock_db)

    # Assert
    assert e.value.status_code == 404
    assert e.value.detail == "Beat not found"

    # verify
    mock_beat_service.get_beat.assert_called_once_with(beat_id, mock_db)


def test_get_beats():
    """
    Test the get_beats method.

    Verifies that the get_beats method returns all beats.
    """
    # Arrange
    beatsheet_id = 1
    beats = [schemas.Beat(id=1, description="Test Beat 1"), schemas.Beat(id=2, description="Test Beat 2")]

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_beat_service = MagicMock(spec=BeatService)
    beat_api.beat_service = mock_beat_service
    mock_beat_service.get_all_beat.return_value = beats

    # Act
    retrieved_beats = beat_api.get_beats(beatsheet_id, mock_db)

    # Assert
    assert len(retrieved_beats) == 2
    assert retrieved_beats[0].description == "Test Beat 1"
    assert retrieved_beats[1].description == "Test Beat 2"

    # verify
    mock_beat_service.get_all_beat.assert_called_once_with(mock_db)


def test_create_beat():
    """
    Test the create_beat method.

    Verifies that the create_beat method creates a new beat.
    """
    # Arrange
    beatsheet_id = 1
    beat = schemas.BeatCreate(description="Test Beat")

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_beat_service = MagicMock(spec=BeatService)
    beat_api.beat_service = mock_beat_service
    mock_beatsheet_service = MagicMock(spec=BeatsheetService)
    beat_api.beatsheet_service = mock_beatsheet_service

    mock_beatsheet_service.get_beatsheet.return_value = schemas.BeatSheet(id=beatsheet_id, title="Test Beatsheet")
    mock_beat_service.create_beat.return_value = schemas.Beat(id=1, description="Test Beat")

    # Act
    created_beat = beat_api.create_beat(beatsheet_id, beat, mock_db)

    # Assert
    assert created_beat.description == "Test Beat"

    # verify
    mock_beatsheet_service.get_beatsheet.assert_called_once_with(beatsheet_id, mock_db)
    mock_beat_service.create_beat.assert_called_once_with(beatsheet_id, beat, mock_db)


def test_create_beat_not_found():
    """
    Test the create_beat method with a non-existent id.

    Verifies that the create_beat method raises a 404 error when the beatsheet is not found.
    """
    # Arrange
    beatsheet_id = 1
    beat = schemas.BeatCreate(description="Test Beat")

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_beat_service = MagicMock(spec=BeatService)
    beat_api.beat_service = mock_beat_service
    mock_beatsheet_service = MagicMock(spec=BeatsheetService)
    beat_api.beatsheet_service = mock_beatsheet_service

    mock_beatsheet_service.get_beatsheet.return_value = None

    # Act
    with pytest.raises(HTTPException) as e:
        beat_api.create_beat(beatsheet_id, beat, mock_db)

    # Assert
    assert e.value.status_code == 404
    assert e.value.detail == "BeatSheet not found"

    # verify
    mock_beatsheet_service.get_beatsheet.assert_called_once_with(beatsheet_id, mock_db)
    mock_beat_service.create_beat.assert_not_called()


def test_update_beat():
    """
    Test the update_beat method.

    Verifies that the update_beat method updates a beat.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 1
    beat = schemas.BeatCreate(description="Updated Test Beat")
    curr_beat = schemas.Beat(id=beat_id, description="Test Beat")

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_beat_service = MagicMock(spec=BeatService)
    beat_api.beat_service = mock_beat_service

    mock_beat_service.get_beat.return_value = curr_beat
    mock_beat_service.update_beat.return_value = schemas.Beat(id=beat_id, description="Updated Test Beat")

    # Act
    updated_beat = beat_api.update_beat(beatsheet_id, beat_id, beat, mock_db)

    # Assert
    assert updated_beat.description == "Updated Test Beat"

    # verify
    mock_beat_service.get_beat.assert_called_once_with(beat_id, mock_db)
    mock_beat_service.update_beat.assert_called_once_with(curr_beat, beat, mock_db)


def test_update_beat_not_found():
    """
    Test the update_beat method with a non-existent id.

    Verifies that the update_beat method raises a 404 error when the beat is not found.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 999
    beat = schemas.BeatCreate(description="Updated Test Beat")

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_beat_service = MagicMock(spec=BeatService)
    beat_api.beat_service = mock_beat_service
    mock_beat_service.get_beat.return_value = None

    # Act
    with pytest.raises(HTTPException) as e:
        beat_api.update_beat(beatsheet_id, beat_id, beat, mock_db)

    # Assert
    assert e.value.status_code == 404
    assert e.value.detail == "Beat not found"

    # verify
    mock_beat_service.get_beat.assert_called_once_with(beat_id, mock_db)
    mock_beat_service.delete_beat.assert_not_called()


def test_delete_beat():
    """
    Test the delete_beat method.

    Verifies that the delete_beat method deletes a beat.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 1
    curr_beat = schemas.Beat(id=beat_id, description="Test Beat")
    response = {"message": f"Beat with ID {beat_id} deleted successfully"}

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_beat_service = MagicMock(spec=BeatService)
    beat_api.beat_service = mock_beat_service
    mock_beat_service.get_beat.return_value = curr_beat
    mock_beat_service.delete_beat.return_value = None

    # Act
    actual_response = beat_api.delete_beat(beatsheet_id, beat_id, mock_db)

    # Assert
    assert actual_response == response

    # verify
    mock_beat_service.get_beat.assert_called_once_with(beat_id, mock_db)
    mock_beat_service.delete_beat.assert_called_once_with(curr_beat, mock_db)


def test_delete_beat_not_found():
    """
    Test the delete_beat method with a non-existent id.

    Verifies that the delete_beat method raises a 404 error when the beat is not found.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 999

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_beat_service = MagicMock(spec=BeatService)
    beat_api.beat_service = mock_beat_service
    mock_beat_service.get_beat.return_value = None

    # Act
    with pytest.raises(HTTPException) as e:
        beat_api.delete_beat(beatsheet_id, beat_id, mock_db)

    # Assert
    assert e.value.status_code == 404
    assert e.value.detail == "Beat not found"

    # verify
    mock_beat_service.get_beat.assert_called_once_with(beat_id, mock_db)
    mock_beat_service.delete_beat.assert_not_called()
