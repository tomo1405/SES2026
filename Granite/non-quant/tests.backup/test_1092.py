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
    test_data = [
        ([1, 2, 3], '1\n2\n3\n'),
        ([4, 5, 6], '4\n5\n6\n'),
        ([7, 8, 9], '7\n8\n9\n')
    ]

    for expected_result, test_input in test_data:
        with open('test_file.txt', 'w') as f:
            f.write(test_input)

        result = task_func(DIRECTORY)

        assert result == expected_result