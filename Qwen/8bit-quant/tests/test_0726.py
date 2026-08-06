import pytest
from src_0726 import task_func
import os
import glob
import tempfile

def test_task_func():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Set up test files
        test_file1 = os.path.join(temp_dir, 'test1.txt')
        test_file2 = os.path.join(temp_dir, 'test2.txt')
        
        with open(test_file1, 'w', encoding='cp1251') as f:
            f.write('Привет мир')
        
        with open(test_file2, 'w', encoding='cp1251') as f:
            f.write('Hello world')

        # Run the function
        task_func(directory=temp_dir, from_encoding='cp1251', to_encoding='utf8')

        # Check if the files have been converted correctly
        with open(test_file1, 'r', encoding='utf8') as f:
            assert f.read() == 'Привет мир'

        with open(test_file2, 'r', encoding='utf8') as f:
            assert f.read() == 'Hello world'