from app.data.models import BeatSheet, Beat, Act


def test_beatsheet_model():
    """
    Test the BeatSheet model.

    Verifies that the BeatSheet model can be initialized with valid data and that the relationships with Beat are correctly established.
    """
    beatsheet = BeatSheet(title="Test beatsheet")
    assert beatsheet.title == "Test beatsheet"
    assert beatsheet.beats == []


def test_beat_model():
    """
    Test the Beat model.

    Verifies that the Beat model can be initialized with valid data and that the relationships with BeatSheet and Act are correctly established.
    """
    beat = Beat(description="Test beat")
    assert beat.description == "Test beat"
    assert beat.beatsheet_id is None
    assert beat.acts == []


def test_act_model():
    """
    Test the Act model.

    Verifies that the Act model can be initialized with valid data and that the relationships with Beat are correctly established.
    """
    act = Act(description="Test act")
    assert act.description == "Test act"
    assert act.beat_id is None


def test_beatsheet_beat_relationship():
    """
    Test the relationship between BeatSheet and Beat.

    Verifies that a Beat can be added to a BeatSheet and that the relationship is correctly established.
    """
    beatsheet = BeatSheet(title="Test beatsheet")
    beat = Beat(description="Test beat", beatsheet_id=beatsheet.id)
    beatsheet.beats.append(beat)
    assert beatsheet.beats == [beat]
    assert beat.beatsheet_id == beatsheet.id


def test_beat_act_relationship():
    """
    Test the relationship between Beat and Act.

    Verifies that an Act can be added to a Beat and that the relationship is correctly established.
    """
    beat = Beat(description="Test beat")
    act = Act(description="Test act", beat_id=beat.id)
    beat.acts.append(act)
    assert beat.acts == [act]
    assert act.beat_id == beat.id
