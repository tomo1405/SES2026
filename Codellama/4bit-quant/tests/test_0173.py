import pytest
from src_0173 import task_func

def test_task_func():
    # Test case 1: JSON string with valid datetime
    json_data = '{"utc_datetime": "2023-02-13T12:34:56"}'
    assert task_func(json_data) == False

    # Test case 2: JSON string with invalid datetime
    json_data = '{"utc_datetime": "2023-02-13T12:34:56"}'
    with pytest.raises(Exception):
        task_func(json_data)

    # Test case 3: JSON string with valid datetime on weekend
    json_data = '{"utc_datetime": "2023-02-13T12:34:56"}'
    assert task_func(json_data) == True

    # Test case 4: JSON string with invalid datetime on weekend
    json_data = '{"utc_datetime": "2023-02-13T12:34:56"}'
    with pytest.raises(Exception):
        task_func(json_data)