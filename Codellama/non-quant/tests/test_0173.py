import pytest
from src_0173 import task_func

def test_task_func():
    # Test case 1: Valid JSON string
    json_data = '{"utc_datetime": "2023-02-13T12:00:00"}'
    assert task_func(json_data) == False

    # Test case 2: Invalid JSON string
    json_data = '{"utc_datetime": "2023-02-13T12:00:00"'
    with pytest.raises(Exception):
        task_func(json_data)

    # Test case 3: Valid JSON string with weekend date
    json_data = '{"utc_datetime": "2023-02-13T12:00:00"}'
    assert task_func(json_data) == True

    # Test case 4: Valid JSON string with non-weekend date
    json_data = '{"utc_datetime": "2023-02-13T12:00:00"}'
    assert task_func(json_data) == False