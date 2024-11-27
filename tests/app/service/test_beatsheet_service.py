import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from app.data import models, schemas
from app.repository.beatsheet_repo import BeatsheetRepository
from app.service.beatsheet_service import BeatsheetService


class TestBeatsheetServiceWithMocks(unittest.TestCase):

    def setUp(self):
        # Mock BeatsheetRepository and Session
        self.mock_repo = MagicMock(spec=BeatsheetRepository)
        self.mock_db = MagicMock(spec=Session)
        self.service = BeatsheetService()

    def test_create_beatsheet(self):
        # Arrange
        beatsheet_data = schemas.BeatSheetCreate(
            title="Sample title"
        )
        expected_beatsheet = models.BeatSheet(
            title=beatsheet_data.title,
        )
        self.mock_repo.create.return_value = expected_beatsheet

        # Act
        with unittest.mock.patch('app.service.beatsheet_service.beatsheet_repo', self.mock_repo):
            result = self.service.create_beatsheet(beatsheet_data, self.mock_db)

        # Assert
        self.assertEqual(result, expected_beatsheet)

    def test_get_beatsheet(self):
        # Arrange
        beatsheet_id = 42
        expected_beatsheet = models.BeatSheet(id=beatsheet_id)
        self.mock_repo.get_by_id.return_value = expected_beatsheet

        # Act
        with unittest.mock.patch('app.service.beatsheet_service.beatsheet_repo', self.mock_repo):
            result = self.service.get_beatsheet(beatsheet_id, self.mock_db)

        # Assert
        self.mock_repo.get_by_id.assert_called_once_with(
            models.BeatSheet, models.BeatSheet.id, beatsheet_id, self.mock_db)
        self.assertEqual(result, expected_beatsheet)

    def test_update_beatsheet(self):
        # Arrange
        current_beatsheet = models.BeatSheet(
            title="Old title"
        )
        updated_data = schemas.BeatSheetCreate(
            title="Updated title"
        )
        updated_beatsheet = models.BeatSheet(
            title=updated_data.title
        )
        self.mock_repo.update.return_value = updated_beatsheet

        # Act
        with unittest.mock.patch('app.service.beatsheet_service.beatsheet_repo', self.mock_repo):
            result = self.service.update_beatsheet(current_beatsheet, updated_data, self.mock_db)

        # Assert
        self.mock_repo.update.assert_called_once_with(current_beatsheet, self.mock_db)
        self.assertEqual(result.title, updated_data.title)

    def test_delete_beatsheet(self):
        # Arrange
        beatsheet_to_delete = models.BeatSheet(id=42)
        self.mock_repo.delete.return_value = True

        # Act
        with unittest.mock.patch('app.service.beatsheet_service.beatsheet_repo', self.mock_repo):
            result = self.service.delete_beatsheet(beatsheet_to_delete, self.mock_db)

        # Assert
        self.mock_repo.delete.assert_called_once_with(beatsheet_to_delete, self.mock_db)
        self.assertTrue(result)

    def test_get_beatsheets(self):
        # Arrange
        expected_beatsheets = [models.BeatSheet(id=1), models.BeatSheet(id=2)]
        self.mock_repo.get_all.return_value = expected_beatsheets

        # Act
        with unittest.mock.patch('app.service.beatsheet_service.beatsheet_repo', self.mock_repo):
            result = self.service.get_all_beatsheets(self.mock_db)

        # Assert
        self.mock_repo.get_all.assert_called_once_with(models.BeatSheet, self.mock_db)
        self.assertEqual(result, expected_beatsheets)


if __name__ == '__main__':
    unittest.main()
