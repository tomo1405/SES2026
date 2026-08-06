import pytest
from src_0328 import task_func
import os

@pytest.fixture
def create_temp_csv_file(tmpdir):
    content = "Hello, world!\nThis is a test.\n(Another line)"
    file_path = tmpdir.join("test.csv")
    with open(file_path, 'w') as file:
        file.write(content)
    return str(file_path)

def test_task_func_with_default_pattern(create_temp_csv_file):
    result = task_func(create_temp_csv_file)
    expected = {
        'Hello': 1,
        ',': 1,
        'world': 1,
        '!': 1,
        'This': 1,
        'is': 1,
        'a': 1,
        'test': 1,
        '.': 1,
        'Another': 1,
        'line': 1
    }
    assert result == expected

def test_task_func_with_custom_pattern(create_temp_csv_file):
    custom_pattern = r'\b\w+\b'
    result = task_func(create_temp_csv_file, custom_pattern)
    expected = {
        'Hello': 1,
        'world': 1,
        'This': 1,
        'is': 1,
        'a': 1,
        'test': 1,
        'Another': 1,
        'line': 1
    }
    assert result == expected

def test_task_func_with_empty_file(tmpdir):
    file_path = tmpdir.join("empty.csv")
    with open(file_path, 'w') as file:
        pass
    result = task_func(str(file_path))
    assert result == {}

def test_task_func_with_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent.csv")