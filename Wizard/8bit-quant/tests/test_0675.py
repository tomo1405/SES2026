python
import pandas as pd
import os
import pytest

def task_func(filename):
    if not os.path.exists(filename):
        return filename

    # Check if empty
    with open(filename, 'r') as file:
        if not file.read(1):
            return filename

    df = pd.read_csv(filename)
    df = df.iloc[::-1]
    df.to_csv(filename, index=False)

    with open(filename, 'r+') as file:
        file.seek(0)

    return filename

def test_task_func():
    # Test case 1: file exists and is not empty
    with open('test.csv', 'w') as file:
        file.write('1,2,3\n4,5,6\n')
    assert task_func('test.csv') == 'test.csv'

    # Test case 2: file exists and is empty
    with open('test2.csv', 'w') as file:
        pass
    assert task_func('test2.csv') == 'test2.csv'

    # Test case 3: file does not exist
    assert task_func('test3.csv') == 'test3.csv'