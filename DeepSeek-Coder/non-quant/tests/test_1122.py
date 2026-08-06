import pytest
from src_1122 import task_func

@pytest.fixture
def sample_data():
    return "This is a sample string with urls like http://example.com and https://example.org"

def test_task_func(sample_data):
    result = task_func("API_KEY")
    assert isinstance(result, dict), "The result should be a dictionary"
    assert len(result) > 0, "The result dictionary should not be empty"
    for key, value in result.items():
        assert "status" in value, "Each value should contain a status key"
        assert "country" in value, "Each value should contain a country key"