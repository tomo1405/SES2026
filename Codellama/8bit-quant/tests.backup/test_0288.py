import pytest
from src_0288 import task_func

def test_task_func():
    directory = 'test_directory'
    filename = 'test_file.json'
    total_words = task_func(filename, directory)
    assert total_words == 10

    with open(filename, 'r') as file:
        word_counts = json.load(file)
    assert word_counts == {'word1': 2, 'word2': 3, 'word3': 4, 'word4': 5}