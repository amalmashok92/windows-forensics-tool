from forensics import registry_analysis

def test_registry_analysis():
    assert callable(registry_analysis.extract_registry_info)