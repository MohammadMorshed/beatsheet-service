from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.api import beatsheet_api
from app.data import schemas, models
from app.service.beatsheet_service import BeatsheetService


def test_get_beatsheet():
    """
    Test the get_beatsheet method.

    Verifies that the get_beatsheet method returns a beatsheet by id.
    """
    # Arrange
    beatsheet_id = 1
    beatsheet = schemas.BeatSheet(id=beatsheet_id, title="Test Beatsheet")

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_service = MagicMock(spec=BeatsheetService)
    beatsheet_api.service = mock_service
    mock_service.get_beatsheet.return_value = beatsheet

    # Act
    retrieved_beatsheet = beatsheet_api.get_beatsheet(beatsheet_id, mock_db)

    # Assert
    assert retrieved_beatsheet.title == "Test Beatsheet"

    # verify
    mock_service.get_beatsheet.assert_called_once_with(beatsheet_id, mock_db)


def test_get_beatsheet_not_found():
    """
    Test the get_beatsheet method with a non-existent id.

    Verifies that the get_beatsheet method returns None when the beatsheet is not found.
    """
    # Arrange
    beatsheet_id = 1

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_service = MagicMock(spec=BeatsheetService)
    beatsheet_api.service = mock_service
    mock_service.get_beatsheet.return_value = None

    # Act
    with pytest.raises(HTTPException) as e:
        beatsheet_api.get_beatsheet(beatsheet_id, mock_db)

    # Assert
    assert e.value.status_code == 404
    assert e.value.detail == "BeatSheet not found"

    # verify
    mock_service.get_beatsheet.assert_called_once_with(beatsheet_id, mock_db)


def test_get_all_beatsheets():
    """
    Test the get_all_beatsheets method.

    Verifies that the get_all_beatsheets method returns all beatsheets.
    """
    # Arrange
    beatsheets = [schemas.BeatSheet(id=1, title="Test Beatsheet 1"), schemas.BeatSheet(id=2, title="Test Beatsheet 2")]

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_service = MagicMock(spec=BeatsheetService)
    beatsheet_api.service = mock_service
    mock_service.get_all_beatsheets.return_value = beatsheets

    # Act
    retrieved_beatsheets = beatsheet_api.get_all_beatsheets(mock_db)

    # Assert
    assert len(retrieved_beatsheets) == 2
    assert retrieved_beatsheets[0].title == "Test Beatsheet 1"
    assert retrieved_beatsheets[1].title == "Test Beatsheet 2"

    # verify
    mock_service.get_all_beatsheets.assert_called_once_with(mock_db)


def test_create_beatsheet():
    """
    Test the create_beatsheet method.

    Verifies that the create_beatsheet method creates a new beatsheet.
    """
    # Arrange
    beatsheet = schemas.BeatSheetCreate(title="Test Beatsheet")

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_service = MagicMock(spec=BeatsheetService)
    beatsheet_api.service = mock_service
    mock_service.create_beatsheet.return_value = schemas.BeatSheet(id=1, title="Test Beatsheet")

    # Act
    created_beatsheet = beatsheet_api.create_beatsheet(beatsheet, mock_db)

    # Assert
    assert created_beatsheet.title == "Test Beatsheet"

    # verify
    mock_service.create_beatsheet.assert_called_once_with(beatsheet, mock_db)


def test_update_beatsheet():
    """
    Test the update_beatsheet method.

    Verifies that the update_beatsheet method updates a beatsheet.
    """
    # Arrange
    beatsheet_id = 1
    beatsheet = schemas.BeatSheetCreate(title="Updated Test Beatsheet")
    curr_beatsheet = models.BeatSheet(id=beatsheet_id, title="Test Beatsheet")

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_service = MagicMock(spec=BeatsheetService)
    beatsheet_api.service = mock_service
    mock_service.get_beatsheet.return_value = curr_beatsheet
    mock_service.update_beatsheet.return_value = schemas.BeatSheet(id=beatsheet_id, title="Updated Test Beatsheet")

    # Act
    updated_beatsheet = beatsheet_api.update_beatsheet(beatsheet_id, beatsheet, mock_db)

    # Assert
    assert updated_beatsheet.title == "Updated Test Beatsheet"

    # verify
    mock_service.get_beatsheet.assert_called_once_with(beatsheet_id, mock_db)
    mock_service.update_beatsheet.assert_called_once_with(curr_beatsheet, beatsheet, mock_db)


def test_update_beatsheet_not_found():
    """
    Test the update_beatsheet method with a non-existent id.

    Verifies that the update_beatsheet method raises a 404 error when the beatsheet is not found.
    """
    # Arrange
    beatsheet_id = 999
    beatsheet = schemas.BeatSheetCreate(title="Updated Test Beatsheet")

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_service = MagicMock(spec=BeatsheetService)
    beatsheet_api.service = mock_service
    mock_service.get_beatsheet.return_value = None

    # Act
    with pytest.raises(HTTPException) as e:
        beatsheet_api.update_beatsheet(beatsheet_id, beatsheet, mock_db)

    # Assert
    assert e.value.status_code == 404
    assert e.value.detail == "BeatSheet not found"

    # verify
    mock_service.get_beatsheet.assert_called_once_with(beatsheet_id, mock_db)


def test_delete_beatsheet():
    """
    Test the delete_beatsheet method.

    Verifies that the delete_beatsheet method deletes a beatsheet.
    """
    # Arrange
    beatsheet_id = 1
    curr_beatsheet = models.BeatSheet(id=beatsheet_id, title="Test Beatsheet")
    expected_response = {"message": f"Beatsheet with ID {beatsheet_id} deleted successfully"}

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_service = MagicMock(spec=BeatsheetService)
    beatsheet_api.service = mock_service
    mock_service.get_beatsheet.return_value = curr_beatsheet
    mock_service.delete_beatsheet.return_value = curr_beatsheet

    # Act
    response = beatsheet_api.delete_beatsheet(beatsheet_id, mock_db)

    # Assert
    assert response == expected_response

    # verify
    mock_service.get_beatsheet.assert_called_once_with(beatsheet_id, mock_db)
    mock_service.delete_beatsheet.assert_called_once_with(curr_beatsheet, mock_db)


def test_delete_beatsheet_not_found():
    """
    Test the delete_beatsheet method with a non-existent id.

    Verifies that the delete_beatsheet method raises a 404 error when the beatsheet is not found.
    """
    # Arrange
    beatsheet_id = 999

    # mocks
    mock_db = MagicMock(spec=Session)
    mock_service = MagicMock(spec=BeatsheetService)
    beatsheet_api.service = mock_service
    mock_service.get_beatsheet.return_value = None

    # Act
    with pytest.raises(HTTPException) as e:
        beatsheet_api.delete_beatsheet(beatsheet_id, mock_db)

    # Assert
    assert e.value.status_code == 404
    assert e.value.detail == "BeatSheet not found"

    # verify
    mock_service.get_beatsheet.assert_called_once_with(beatsheet_id, mock_db)
