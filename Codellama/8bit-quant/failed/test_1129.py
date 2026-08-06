import pytest
from src_1129 import task_func

def test_task_func():
    file_path = "test_data.json"
    unknown_key = "key1"
    expected_hashed_str = "hashed_value"

    new_file_path = task_func(file_path, unknown_key)

    with open(new_file_path, 'r') as f:
        actual_hashed_str = f.read()

    assert actual_hashed_str == expected_hashed_str