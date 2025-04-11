from forensics import event_logs

def test_event_logs():
    assert callable(event_logs.collect_event_logs)