from app.data.database import Settings, SessionLocal, Base, get_db


def test_settings():
    """
    Test the Settings class.

    Verifies that the Settings class can be initialized with valid data and that the database URL is correctly set.
    """
    settings = Settings()
    assert settings.DATABASE_URL is not None


def test_session_local():
    """
    Test the SessionLocal class.

    Verifies that the SessionLocal class can be initialized and that a database session can be created.
    """
    session = SessionLocal()
    assert session is not None


def test_base():
    """
    Test the Base class.

    Verifies that the Base class can be initialized and that it is a subclass of declarative_base.
    """
    assert Base is not None


def test_get_db():
    """
    Test the get_db function.

    Verifies that the get_db function returns a database session and that the session is correctly closed after use.
    """
    db = get_db()
    assert db is not None
    db.close()
