import pytest
from src_1094 import task_func

def test_task_func():
    # Test case 1: Empty file
    with pytest.raises(ValueError):
        task_func("")

    # Test case 2: Non-existent file
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.txt")

    # Test case 3: Valid file with no matches
    with pytest.raises(ValueError):
        task_func("tests/test_data/test_data_1.txt")

    # Test case 4: Valid file with matches
    results = task_func("tests/test_data/test_data_2.txt")
    assert results == [{"key1": "value1"}, {"key2": "value2"}]

    # Test case 5: Valid file with nested matches
    results = task_func("tests/test_data/test_data_3.txt")
    assert results == [{"key1": "value1"}, {"key2": "value2"}, {"key3": {"key31": "value31"}}]