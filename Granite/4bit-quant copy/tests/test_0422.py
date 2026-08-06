import pytest
from src_0422 import task_func

def test_task_func():
    url = "https://example.com/api"
    directory = "/path/to/directory"
    metadata = {"key": "value"}
    expected_status_codes = [200, 201, 202]

    actual_status_codes = task_func(url, directory, metadata)

    assert actual_status_codes == expected_status_codes