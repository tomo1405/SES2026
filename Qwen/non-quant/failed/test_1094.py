import pytest
from src_1094 import task_func
import os

@pytest.fixture
def create_temp_file(tmp_path):
    content = '{"key1": "value1", "key2": {"nested_key1": "nested_value1"}}\n{"key3": "value3"}'
    temp_file = tmp_path / "temp.txt"
    temp_file.write_text(content)
    yield temp_file
    os.remove(temp_file)

def test_task_func(create_temp_file):
    result = task_func(str(create_temp_file))
    expected_result = [
        {'key1': 'value1', 'key2': {'nested_key1': 'nested_value1'}},
        {'key3': 'value3'}
    ]
    assert result == expected_result

def test_task_func_empty_file(tmp_path):
    temp_file = tmp_path / "empty.txt"
    temp_file.touch()
    result = task_func(str(temp_file))
    assert result == []

def test_task_func_no_dicts(tmp_path):
    content = "This is a test file without any dictionaries."
    temp_file = tmp_path / "no_dicts.txt"
    temp_file.write_text(content)
    result = task_func(str(temp_file))
    assert result == []

def test_task_func_nested_dicts(tmp_path):
    content = '{"a": {"b": {"c": "d"}}}\n{"e": "f"}'
    temp_file = tmp_path / "nested_dicts.txt"
    temp_file.write_text(content)
    result = task_func(str(temp_file))
    expected_result = [
        {'a': {'b': {'c': 'd'}}},
        {'e': 'f'}
    ]
    assert result == expected_result