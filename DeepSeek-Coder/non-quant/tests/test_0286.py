import pytest
from src_0286 import task_func

@pytest.fixture
def setup():
    url = "http://example.com"
    form_id = 0
    data = {"key1": "value1", "key2": "value2"}
    return url, form_id, data

def test_task_func(setup):
    url, form_id, data = setup
    result = task_func(url, form_id, data)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) > 0, "The result should not be empty"