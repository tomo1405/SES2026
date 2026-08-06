import pytest
from src_0288 import task_func

def test_task_func():
    # Test case 1: Test with a single file
    directory = 'tests/test_data'
    filename = 'test_output.json'
    total_words = task_func(filename, directory)
    assert total_words == 10
    with open(filename, 'r') as file:
        word_counts = json.load(file)
    assert word_counts == {'hello': 2, 'world': 3, 'python': 2, 'testing': 1}

    # Test case 2: Test with multiple files
    directory = 'tests/test_data'
    filename = 'test_output.json'
    total_words = task_func(filename, directory)
    assert total_words == 10
    with open(filename, 'r') as file:
        word_counts = json.load(file)
    assert word_counts == {'hello': 2, 'world': 3, 'python': 2, 'testing': 1}

    # Test case 3: Test with a file that does not exist
    directory = 'tests/test_data'
    filename = 'test_output.json'
    total_words = task_func(filename, directory)
    assert total_words == 0
    with open(filename, 'r') as file:
        word_counts = json.load(file)
    assert word_counts == {}

    # Test case 4: Test with a directory that does not exist
    directory = 'tests/test_data'
    filename = 'test_output.json'
    total_words = task_func(filename, directory)
    assert total_words == 0
    with open(filename, 'r') as file:
        word_counts = json.load(file)
    assert word_counts == {}