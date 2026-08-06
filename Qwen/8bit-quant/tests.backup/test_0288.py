import pytest
from src_0288 import task_func
from collections import Counter
import os
import json
import tempfile

def test_task_func():
    # Create a temporary directory and some text files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create two text files with some content
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        
        with open(file1_path, 'w') as f:
            f.write("hello world hello")
        
        with open(file2_path, 'w') as f:
            f.write("world test test test")
        
        # Define the output file path
        output_file_path = os.path.join(temp_dir, 'output.json')
        
        # Call the function
        total_words = task_func(output_file_path, temp_dir)
        
        # Check the total number of words
        assert total_words == 9
        
        # Check the contents of the output JSON file
        with open(output_file_path, 'r') as f:
            word_counts = json.load(f)
        
        expected_word_counts = {
            'hello': 2,
            'world': 2,
            'test': 3
        }
        
        assert word_counts == expected_word_counts

def test_task_func_no_txt_files():
    # Create a temporary directory with no text files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Define the output file path
        output_file_path = os.path.join(temp_dir, 'output.json')
        
        # Call the function
        total_words = task_func(output_file_path, temp_dir)
        
        # Check the total number of words
        assert total_words == 0
        
        # Check the contents of the output JSON file
        with open(output_file_path, 'r') as f:
            word_counts = json.load(f)
        
        assert word_counts == {}

def test_task_func_empty_directory():
    # Create an empty temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Define the output file path
        output_file_path = os.path.join(temp_dir, 'output.json')
        
        # Call the function
        total_words = task_func(output_file_path, temp_dir)
        
        # Check the total number of words
        assert total_words == 0
        
        # Check the contents of the output JSON file
        with open(output_file_path, 'r') as f:
            word_counts = json.load(f)
        
        assert word_counts == {}