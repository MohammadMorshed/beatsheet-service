from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.api import act_api
from app.data import schemas
from app.service.act_service import ActService
from app.service.beat_service import BeatService


def test_get_act():
    """
    Test the get_act method.

    Verifies that the get_act method returns an act by id.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 1
    act_id = 1
    act = schemas.Act(
        id=act_id,
        description="Test Act",
        duration=30,
        camera_angle="45")

    # Mocks
    mock_db = MagicMock(spec=Session)
    mock_act_service = MagicMock(spec=ActService)
    act_api.act_service = mock_act_service
    mock_act_service.get_act.return_value = act

    # Act
    retrieved_act = act_api.get_act(beatsheet_id, beat_id, act_id, mock_db)

    # Assert
    assert retrieved_act == act

    # Verify
    mock_act_service.get_act.assert_called_once_with(act_id, mock_db)


def test_get_act_not_found():
    """
    Test the get_act method with a non-existent id.

    Verifies that the get_act method raises a 404 error when the act is not found.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 1
    act_id = 999

    # Mocks
    mock_db = MagicMock(spec=Session)
    mock_act_service = MagicMock(spec=ActService)
    act_api.act_service = mock_act_service
    mock_act_service.get_act.return_value = None

    # Act
    with pytest.raises(HTTPException) as e:
        act_api.get_act(beatsheet_id, beat_id, act_id, mock_db)

    # Assert
    assert e.value.status_code == 404
    assert e.value.detail == "Act not found"

    # Verify
    mock_act_service.get_act.assert_called_once_with(act_id, mock_db)


def test_create_act():
    """
    Test the create_act method.

    Verifies that the create_act method creates a new act.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 1
    act = schemas.ActCreate(
        description="Test Act",
        duration=30,
        camera_angle="45")

    # Mocks
    mock_db = MagicMock(spec=Session)
    mock_act_service = MagicMock(spec=ActService)
    act_api.act_service = mock_act_service
    mock_beat_service = MagicMock(spec=BeatService)
    act_api.beat_service = mock_beat_service

    mock_beat_service.get_beat.return_value = schemas.Beat(
        id=beat_id, description="Test Beat")

    mock_act_service.create_act.return_value = schemas.Act(
        id=1,
        description="Test Act",
        duration=30,
        camera_angle="45")

    # Act
    created_act = act_api.create_act(beatsheet_id, beat_id, act, mock_db)

    # Assert
    assert created_act.description == "Test Act"

    # Verify
    mock_beat_service.get_beat.assert_called_once_with(beat_id, mock_db)
    mock_act_service.create_act.assert_called_once_with(beat_id, act, mock_db)


def test_create_act_not_found():
    """
    Test the create_act method with a non-existent beat.

    Verifies that the create_act method raises a 404 error when the beat is not found.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 999
    act = schemas.ActCreate(
        description="Test Act",
        duration=30,
        camera_angle="45")

    # Mocks
    mock_db = MagicMock(spec=Session)
    mock_act_service = MagicMock(spec=ActService)
    act_api.act_service = mock_act_service
    mock_beat_service = MagicMock(spec=BeatService)
    act_api.beat_service = mock_beat_service

    mock_beat_service.get_beat.return_value = None

    # Act
    with pytest.raises(HTTPException) as e:
        act_api.create_act(beatsheet_id, beat_id, act, mock_db)

    # Assert
    assert e.value.status_code == 404
    assert e.value.detail == "Beat not found"

    # Verify
    mock_beat_service.get_beat.assert_called_once_with(beat_id, mock_db)
    mock_act_service.create_act.assert_not_called()


def test_update_act():
    """
    Test the update_act method.

    Verifies that the update_act method updates an act.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 1
    act_id = 1
    act = schemas.ActCreate(
        description="Updated Test Act",
        duration=30,
        camera_angle="45")

    curr_act = schemas.Act(
        id=act_id,
        description="Test Act",
        duration=30,
        camera_angle="45")

    # Mocks
    mock_db = MagicMock(spec=Session)
    mock_act_service = MagicMock(spec=ActService)
    act_api.act_service = mock_act_service

    mock_act_service.get_act.return_value = curr_act
    mock_act_service.update_act.return_value = schemas.Act(
        id=act_id,
        description="Updated Test Act",
        duration=30,
        camera_angle="45")

    # Act
    updated_act = act_api.update_act(beatsheet_id, beat_id, act_id, act, mock_db)

    # Assert
    assert updated_act.description == "Updated Test Act"

    # Verify
    mock_act_service.get_act.assert_called_once_with(act_id, mock_db)
    mock_act_service.update_act.assert_called_once_with(curr_act, act, mock_db)


def test_update_act_not_found():
    """
    Test the update_act method with a non-existent id.

    Verifies that the update_act method raises a 404 error when the act is not found.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 1
    act_id = 999
    act = schemas.ActCreate(
        description="Updated Test Act",
        duration=30,
        camera_angle="45")

    # Mocks
    mock_db = MagicMock(spec=Session)
    mock_act_service = MagicMock(spec=ActService)
    act_api.act_service = mock_act_service
    mock_act_service.get_act.return_value = None

    # Act
    with pytest.raises(HTTPException) as e:
        act_api.update_act(beatsheet_id, beat_id, act_id, act, mock_db)

    # Assert
    assert e.value.status_code == 404
    assert e.value.detail == "Act not found"

    # Verify
    mock_act_service.get_act.assert_called_once_with(act_id, mock_db)
    mock_act_service.update_act.assert_not_called()


def test_delete_act():
    """
    Test the delete_act method.

    Verifies that the delete_act method deletes an act.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 1
    act_id = 1
    curr_act = schemas.Act(
        id=act_id,
        description="Test Act",
        duration=30,
        camera_angle="45")

    response = {"message": f"Act with ID {act_id} deleted successfully"}

    # Mocks
    mock_db = MagicMock(spec=Session)
    mock_act_service = MagicMock(spec=ActService)
    act_api.act_service = mock_act_service
    mock_act_service.get_act.return_value = curr_act
    mock_act_service.delete_act.return_value = None

    # Act
    actual_response = act_api.delete_act(beatsheet_id, beat_id, act_id, mock_db)

    # Assert
    assert actual_response == response

    # Verify
    mock_act_service.get_act.assert_called_once_with(act_id, mock_db)
    mock_act_service.delete_act.assert_called_once_with(curr_act, mock_db)


def test_delete_act_not_found():
    """
    Test the delete_act method with a non-existent id.

    Verifies that the delete_act method raises a 404 error when the act is not found.
    """
    # Arrange
    beatsheet_id = 1
    beat_id = 1
    act_id = 999

    # Mocks
    mock_db = MagicMock(spec=Session)
    mock_act_service = MagicMock(spec=ActService)
    act_api.act_service = mock_act_service
    mock_act_service.get_act.return_value = None

    # Act
    with pytest.raises(HTTPException) as e:
        act_api.delete_act(beatsheet_id, beat_id, act_id, mock_db)

    # Assert
    assert e.value.status_code == 404
    assert e.value.detail == "Act not found"

    # Verify
    mock_act_service.get_act.assert_called_once_with(act_id, mock_db)
    mock_act_service.delete_act.assert_not_called()
