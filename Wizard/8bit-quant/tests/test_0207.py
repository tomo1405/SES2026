python
import csv
import json
import os
import pytest

from src_0207 import task_func

def test_task_func():
    # Test case 1: Valid input file
    input_file = 'input.csv'
    expected_output_file = 'input.json'
    with open(input_file, 'w') as f:
        f.write('name,age\nJohn,30\nJane,25')
    assert task_func(input_file) == expected_output_file
    os.remove(input_file)
    os.remove(expected_output_file)

    # Test case 2: Invalid input file
    input_file = 'input.csv'
    with open(input_file, 'w') as f:
        f.write('name,age\nJohn,30\nJane,25')
    with pytest.raises(FileNotFoundError):
        task_func('invalid_file.csv')
    os.remove(input_file)