import json
from datetime import datetime
from src_0173 import task_func
import pytest

def test_task_func():
    # Test case 1: valid JSON data with Saturday or Sunday datetime
    json_data = '{"utc_datetime": "2023-01-01T12:00:00"}'
    assert task_func(json_data) is True

    # Test case 2: valid JSON data with Monday datetime
    json_data = '{"utc_datetime": "2023-01-03T12:00:00"}'
    assert task_func(json_data) is False

    # Test case 3: invalid JSON data
    json_data = '{"utc_datetime": "2023-01-01"}'
    with pytest.raises(Exception):
        task_func(json_data)

    # Test case 4: empty JSON data
    json_data = '{}'
    with pytest.raises(Exception):
        task_func(json_data)