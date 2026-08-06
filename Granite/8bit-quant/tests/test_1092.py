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
        ({'a': 1, 'b': 2}, "{'a': 1, 'b': 2}\n"),
        ([4.5, 'hello'], '4.5\n"hello"\n')
    ]

    for expected_output, input_data in test_data:
        with open('test_file.txt', 'w') as f:
            f.write(input_data)

        assert task_func(DIRECTORY) == [expected_output]

    os.remove('test_file.txt')