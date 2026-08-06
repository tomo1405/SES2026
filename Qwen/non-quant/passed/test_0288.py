import pytest
from src_0288 import task_func
from collections import Counter
import os
import json
import tempfile

def test_task_func():
    # Create a temporary directory and some text files for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        non_txt_path = os.path.join(temp_dir, 'non_txt_file.txt')

        with open(file1_path, 'w') as f:
            f.write("hello world hello")

        with open(file2_path, 'w') as f:
            f.write("world python")

        with open(non_txt_path, 'w') as f:
            f.write("non text file")

        # Define the output file path
        output_file_path = os.path.join(temp_dir, 'output.json')

        # Call the function
        total_words = task_func(output_file_path, temp_dir)

        # Check the total number of words
        assert total_words == 6

        # Check the content of the output JSON file
        with open(output_file_path, 'r') as f:
            word_counts = json.load(f)

        expected_word_counts = {
            "hello": 2,
            "world": 2,
            "python": 1
        }

        assert word_counts == expected_word_counts