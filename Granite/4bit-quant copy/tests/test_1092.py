import ast
import os
import glob
import pytest

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
    test_directory = 'test_data'
    test_files = ['test1.txt', 'test2.txt', 'test3.txt']
    expected_results = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    for i, test_file in enumerate(test_files):
        with open(os.path.join(test_directory, test_file), 'w') as f:
            for result in expected_results[i]:
                f.write(str(result) + '\n')

    results = task_func(test_directory)

    assert results == expected_results

    for test_file in test_files:
        os.remove(os.path.join(test_directory, test_file))