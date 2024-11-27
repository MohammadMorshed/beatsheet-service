import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from app.data import models, schemas
from app.repository.beat_repo import BeatRepository
from app.service.beat_service import BeatService


class TestBeatServiceWithMocks(unittest.TestCase):

    def setUp(self):
        # Mock BeatRepository and Session
        self.mock_repo = MagicMock(spec=BeatRepository)
        self.mock_db = MagicMock(spec=Session)
        self.service = BeatService()

    def test_create_beat(self):
        # Arrange
        beatsheet_id = 1
        beat_data = schemas.BeatCreate(
            description="Sample description",
            timestamp="2024-11-25T10:00:00"
        )
        expected_beat = models.Beat(
            description=beat_data.description,
            timestamp=beat_data.timestamp,
            beatsheet_id=beatsheet_id
        )
        self.mock_repo.create.return_value = expected_beat

        # Act
        with unittest.mock.patch('app.service.beat_service.beat_repo', self.mock_repo):
            result = self.service.create_beat(beatsheet_id, beat_data, self.mock_db)

        # Assert
        self.assertEqual(result, expected_beat)

    def test_get_beat(self):
        # Arrange
        beat_id = 42
        expected_beat = models.Beat(id=beat_id)
        self.mock_repo.get_by_id.return_value = expected_beat

        # Act
        with unittest.mock.patch('app.service.beat_service.beat_repo', self.mock_repo):
            result = self.service.get_beat(beat_id, self.mock_db)

        # Assert
        self.mock_repo.get_by_id.assert_called_once_with(
            models.Beat, models.Beat.id, beat_id, self.mock_db)
        self.assertEqual(result, expected_beat)

    def test_update_beat(self):
        # Arrange
        current_beat = models.Beat(
            description="Old description",
            timestamp="2024-11-25T09:00:00"
        )
        updated_data = schemas.BeatCreate(
            description="Updated description",
            timestamp="2024-11-25T10:00:00"
        )
        updated_beat = models.Beat(
            description=updated_data.description,
            timestamp=updated_data.timestamp
        )
        self.mock_repo.update.return_value = updated_beat

        # Act
        with unittest.mock.patch('app.service.beat_service.beat_repo', self.mock_repo):
            result = self.service.update_beat(current_beat, updated_data, self.mock_db)

        # Assert
        self.mock_repo.update.assert_called_once_with(current_beat, self.mock_db)
        self.assertEqual(result.description, updated_data.description)
        self.assertEqual(result.timestamp, updated_data.timestamp)

    def test_delete_beat(self):
        # Arrange
        beat_to_delete = models.Beat(id=42)
        self.mock_repo.delete.return_value = True

        # Act
        with unittest.mock.patch('app.service.beat_service.beat_repo', self.mock_repo):
            result = self.service.delete_beat(beat_to_delete, self.mock_db)

        # Assert
        self.mock_repo.delete.assert_called_once_with(beat_to_delete, self.mock_db)
        self.assertTrue(result)

    def test_get_beats(self):
        # Arrange
        expected_beats = [models.Beat(id=1), models.Beat(id=2)]
        self.mock_repo.get_all.return_value = expected_beats

        # Act
        with unittest.mock.patch('app.service.beat_service.beat_repo', self.mock_repo):
            result = self.service.get_all_beat(self.mock_db)

        # Assert
        self.mock_repo.get_all.assert_called_once_with(models.Beat, self.mock_db)
        self.assertEqual(result, expected_beats)


if __name__ == '__main__':
    unittest.main()
