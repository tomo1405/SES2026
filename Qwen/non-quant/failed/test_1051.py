import pytest
from src_1051 import task_func
import os
import hashlib

@pytest.fixture(autouse=True)
def cleanup():
    """Cleanup the directory after each test."""
    yield
    if os.path.exists(DIRECTORY):
        for filename in os.listdir(DIRECTORY):
            os.remove(os.path.join(DIRECTORY, filename))
        os.rmdir(DIRECTORY)

def test_task_func_with_empty_input():
    result = task_func("")
    assert result == []

def test_task_func_with_single_line():
    input_string = "hello"
    expected_hash = hashlib.sha256(input_string.encode()).hexdigest()
    expected_filename = expected_hash[:10] + ".txt"
    expected_filepath = os.path.join(DIRECTORY, expected_filename)

    result = task_func(input_string)
    assert result == [expected_filepath]
    assert os.path.exists(expected_filepath)
    with open(expected_filepath, "r", encoding="utf-8") as file:
        content = file.read()
    assert content == expected_hash

def test_task_func_with_multiple_lines():
    input_string = "hello\nworld"
    lines = input_string.split("\n")
    expected_filepaths = []

    for line in lines:
        line_hash = hashlib.sha256(line.encode()).hexdigest()
        filename = line_hash[:10] + ".txt"
        expected_filepath = os.path.join(DIRECTORY, filename)
        expected_filepaths.append(expected_filepath)

    result = task_func(input_string)
    assert set(result) == set(expected_filepaths)
    for filepath in expected_filepaths:
        assert os.path.exists(filepath)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        assert content == hashlib.sha256(os.path.splitext(os.path.basename(filepath))[0].encode()).hexdigest()

def test_task_func_with_empty_lines():
    input_string = "\n\n"
    result = task_func(input_string)
    assert result == []

def test_task_func_with_directory_creation():
    if os.path.exists(DIRECTORY):
        os.rmdir(DIRECTORY)
    task_func("test")
    assert os.path.exists(DIRECTORY)