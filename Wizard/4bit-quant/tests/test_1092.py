python
import ast
import os
import glob
import pytest

# Constants
DIRECTORY = 'data'

def task_func(directory):
    path = os.path.join(directory, '*.txt')
    files = glob.glob(path)

    results = []
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                results.append(ast.literal_eval(line.strip()))

    return results

def test_task_func():
    # Test case 1
    directory = 'data'
    expected_results = [1, 2, 3, 4, 5]
    results = task_func(directory)
    assert results == expected_results

    # Test case 2
    directory = 'data_2'
    expected_results = []
    results = task_func(directory)
    assert results == expected_results

    # Test case 3
    directory = 'data_3'
    expected_results = [1, 2, 3, 4, 5]
    results = task_func(directory)
    assert results == expected_results