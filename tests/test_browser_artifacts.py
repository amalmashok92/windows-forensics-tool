from forensics import browser_artifacts

def test_browser_artifacts():
    assert callable(browser_artifacts.extract_browser_data)