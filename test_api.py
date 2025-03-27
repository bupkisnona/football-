from src.api import get_fixtures, get_results

def test_get_fixtures():
    assert get_fixtures() is not None

def test_get_results():
    assert get_results() is not None
