import pytest
from src_1121 import task_func

@pytest.fixture
def sample_data():
    return "This is a test string with urls like http://example.com and https://example.org"

def test_task_func(sample_data):
    result = task_func("API_KEY")
    assert isinstance(result, dict), "The result should be a dictionary"
    assert len(result) > 0, "The result dictionary should not be empty"