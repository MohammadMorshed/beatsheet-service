import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from app.data import models, schemas
from app.repository.act_repo import ActRepository
from app.service.act_service import ActService


class TestActServiceWithMocks(unittest.TestCase):

    def setUp(self):
        # Mock ActRepository and Session
        self.mock_repo = MagicMock(spec=ActRepository)
        self.mock_db = MagicMock(spec=Session)
        self.service = ActService()

    def test_create_act(self):
        # Arrange
        beat_id = 1
        act_data = schemas.ActCreate(
            description="Sample description",
            timestamp="2024-11-25T10:00:00",
            duration=120,
            camera_angle="front"
        )
        expected_act = models.Act(
            description=act_data.description,
            timestamp=act_data.timestamp,
            duration=act_data.duration,
            camera_angle=act_data.camera_angle,
            beat_id=beat_id
        )
        self.mock_repo.create.return_value = expected_act

        # Act
        with unittest.mock.patch('app.service.act_service.act_repo', self.mock_repo):
            result = self.service.create_act(beat_id, act_data, self.mock_db)

        # Assert
        self.assertEqual(result, expected_act)

    def test_get_act(self):
        # Arrange
        act_id = 42
        expected_act = models.Act(id=act_id)
        self.mock_repo.get_by_id.return_value = expected_act

        # Act
        with unittest.mock.patch('app.service.act_service.act_repo', self.mock_repo):
            result = self.service.get_act(act_id, self.mock_db)

        # Assert
        self.mock_repo.get_by_id.assert_called_once_with(
            models.Act, models.Act.id, act_id, self.mock_db)
        self.assertEqual(result, expected_act)

    def test_update_act(self):
        # Arrange
        current_act = models.Act(
            description="Old description",
            timestamp="2024-11-25T09:00:00",
            duration=100,
            camera_angle="left"
        )
        updated_data = schemas.ActCreate(
            description="Updated description",
            timestamp="2024-11-25T10:00:00",
            duration=120,
            camera_angle="front"
        )
        updated_act = models.Act(
            description=updated_data.description,
            timestamp=updated_data.timestamp,
            duration=updated_data.duration,
            camera_angle=updated_data.camera_angle
        )
        self.mock_repo.update.return_value = updated_act

        # Act
        with unittest.mock.patch('app.service.act_service.act_repo', self.mock_repo):
            result = self.service.update_act(current_act, updated_data, self.mock_db)

        # Assert
        self.mock_repo.update.assert_called_once_with(current_act, self.mock_db)
        self.assertEqual(result.description, updated_data.description)
        self.assertEqual(result.timestamp, updated_data.timestamp)

    def test_delete_act(self):
        # Arrange
        act_to_delete = models.Act(id=42)
        self.mock_repo.delete.return_value = True

        # Act
        with unittest.mock.patch('app.service.act_service.act_repo', self.mock_repo):
            result = self.service.delete_act(act_to_delete, self.mock_db)

        # Assert
        self.mock_repo.delete.assert_called_once_with(act_to_delete, self.mock_db)
        self.assertTrue(result)

    def test_get_acts(self):
        # Arrange
        expected_acts = [models.Act(id=1), models.Act(id=2)]
        self.mock_repo.get_all.return_value = expected_acts

        # Act
        with unittest.mock.patch('app.service.act_service.act_repo', self.mock_repo):
            result = self.service.get_acts(self.mock_db)

        # Assert
        self.mock_repo.get_all.assert_called_once_with(models.Act, self.mock_db)
        self.assertEqual(result, expected_acts)


if __name__ == '__main__':
    unittest.main()
