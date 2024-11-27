# tests/app/data/test_schemas.py
from datetime import datetime

import pytest
from pydantic import ValidationError

from app.data.schemas import ActBase, ActCreate, Act, BeatBase, BeatCreate, Beat, BeatSheetBase, BeatSheetCreate, \
    BeatSheet


def test_act_base():
    """
    Test ActBase model initialization with valid data.

    Verifies that the ActBase model can be initialized with a valid description and timestamp.
    """
    act = ActBase(
        description="Test act",
        timestamp=datetime.utcnow(),
        duration=123,
        camera_angle="45")

    assert act.description == "Test act"
    assert act.timestamp is not None


def test_act_base_invalid():
    """
    Test ActBase model initialization with invalid data.

    Verifies that the ActBase model raises a ValidationError when initialized with an invalid description.
    """
    with pytest.raises(ValidationError):
        ActBase(description=123)


def test_act_create():
    """
    Test ActCreate model initialization with valid data.

    Verifies that the ActCreate model can be initialized with a valid description.
    """
    act = ActCreate(
        description="Test act",
        duration=123,
        camera_angle="45")

    assert act.description == "Test act"


def test_act():
    """
    Test Act model initialization with valid data.

    Verifies that the Act model can be initialized with a valid id, descriptions.
    """
    act = Act(
        id=1,
        description="Test act",
        duration=123,
        camera_angle="45")

    assert act.id == 1
    assert act.description == "Test act"


def test_beat_base():
    """
    Test BeatBase model initialization with valid data.

    Verifies that the BeatBase model can be initialized with a valid description and timestamp.
    """
    beat = BeatBase(description="Test beat", timestamp=datetime.utcnow())
    assert beat.description == "Test beat"
    assert beat.timestamp is not None


def test_beat_base_invalid():
    """
    Test BeatBase model initialization with invalid data.

    Verifies that the BeatBase model raises a ValidationError when initialized with an invalid description.
    """
    with pytest.raises(ValidationError):
        BeatBase(description=123)


def test_beat_create():
    """
    Test BeatCreate model initialization with valid data.

    Verifies that the BeatCreate model can be initialized with a valid description.
    """
    beat = BeatCreate(description="Test beat")
    assert beat.description == "Test beat"


def test_beat():
    """
    Test Beat model initialization with valid data.

    Verifies that the Beat model can be initialized with a valid id, description, acts.
    """
    beat = Beat(
        id=1,
        description="Test beat",
        acts=[], )

    assert beat.id == 1
    assert beat.description == "Test beat"
    assert beat.acts == []


def test_beatsheet_base():
    """
    Test BeatSheetBase model initialization with valid data.

    Verifies that the BeatSheetBase model can be initialized with a valid title.
    """
    beatsheet = BeatSheetBase(title="Test beatsheet")
    assert beatsheet.title == "Test beatsheet"


def test_beatsheet_base_invalid():
    """
    Test BeatSheetBase model initialization with invalid data.

    Verifies that the BeatSheetBase model raises a ValidationError when initialized with an invalid title.
    """
    with pytest.raises(ValidationError):
        BeatSheetBase(title=123)


def test_beatsheet_create():
    """
    Test BeatSheetCreate model initialization with valid data.

    Verifies that the BeatSheetCreate model can be initialized with a valid title.
    """
    beatsheet = BeatSheetCreate(title="Test beatsheet")
    assert beatsheet.title == "Test beatsheet"


def test_beatsheet():
    """
    Test BeatSheet model initialization with valid data.

    Verifies that the BeatSheet model can be initialized with a valid id, title, beats.
    """
    beatsheet = BeatSheet(
        id=1,
        title="Test beatsheet",
        beats=[])
    assert beatsheet.id == 1
    assert beatsheet.title == "Test beatsheet"
    assert beatsheet.beats == []
