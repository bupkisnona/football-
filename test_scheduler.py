import src.scheduler as scheduler

def test_scheduler():
    assert scheduler.post_fixtures() is None
    assert scheduler.post_results() is None
