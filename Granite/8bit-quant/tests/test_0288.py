import os
import json
from collections import Counter
from tempfile import TemporaryDirectory
from pathlib import Path

import pytest

from src_0288 import task_func

def test_task_func():
    with TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir)
        # Create a sample text file
        sample_text_file = temp_dir / 'sample.txt'
        sample_text_file.write_text('This is a sample text file.')
        # Call the function with the sample text file and the temporary directory
        result = task_func('word_counts.json', temp_dir)
        # Check if the result is a positive integer
        assert isinstance(result, int) and result > 0
        # Check if the word counts file was created
        word_counts_file = temp_dir / 'word_counts.json'
        assert word_counts_file.is_file()
        # Check if the word counts file contains valid JSON data
        with word_counts_file.open() as file:
            word_counts = json.load(file)
        assert isinstance(word_counts, dict)
        assert all(isinstance(word, str) for word in word_counts)
        assert all(isinstance(count, int) and count >= 0 for count in word_counts.values())
        # Check if the total number of words matches the sum of word counts
        assert result == sum(word_counts.values())

def test_task_func_with_invalid_directory():
    with pytest.raises(FileNotFoundError):
        task_func('word_counts.json', 'invalid_directory')

def test_task_func_with_invalid_filename():
    with TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir)
        # Call the function with an invalid filename and the temporary directory
        result = task_func('invalid_filename.json', temp_dir)
        # Check if the result is None
        assert result is None