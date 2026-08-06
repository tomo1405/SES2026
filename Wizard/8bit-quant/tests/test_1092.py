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

# Test cases
def test_task_func():
    # Test case 1
    directory = 'data'
    expected_results = [1, 2, 3, 4, 5]
    assert task_func(directory) == expected_results

    # Test case 2
    directory = 'data2'
    expected_results = []
    assert task_func(directory) == expected_results

    # Test case 3
    directory = 'data'
    expected_results = [1, 2, 3, 4, 5]
    assert task_func(directory) == expected_results

    # Test case 4
    directory = 'data'
    expected_results = [1, 2, 3, 4, 5]
    assert task_func(directory) == expected_results

    # Test case 5
    directory = 'data'
    expected_results = [1, 2, 3, 4, 5]
    assert task_func(directory) == expected_results

    # Test case 6
    directory = 'data'
    expected_results = [1, 2, 3, 4, 5]
    assert task_func(directory) == expected_results

    # Test case 7
    directory = 'data'
    expected_results = [1, 2, 3, 4, 5]
    assert task_func(directory) == expected_results

    # Test case 8
    directory = 'data'
    expected_results = [1, 2, 3, 4, 5]
    assert task_func(directory) == expected_results

    # Test case 9
    directory = 'data'
    expected_results = [1, 2, 3, 4, 5]
    assert task_func(directory) == expected_results

    # Test case 10
    directory = 'data'
    expected_results = [1, 2, 3, 4, 5]
    assert task_func(directory) == expected_results

# Run tests
if __name__ == '__main__':
    pytest.main(['-v', __file__])