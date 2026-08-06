python
import collections
import pandas as pd
import pytest

def task_func(my_tuple, path_csv_files):

    counter = {column: collections.Counter() for column in my_tuple}

    for csv_file in path_csv_files:
        df = pd.read_csv(csv_file)

        for column in my_tuple:
            if column in df:
                counter[column].update(df[column])

    return counter

def test_task_func():
    my_tuple = ('col1', 'col2', 'col3')
    path_csv_files = ['file1.csv', 'file2.csv']

    expected_result = {
        'col1': collections.Counter({'a': 1, 'b': 1}),
        'col2': collections.Counter({'c': 1, 'd': 1}),
        'col3': collections.Counter({'e': 1, 'f': 1})
    }

    result = task_func(my_tuple, path_csv_files)

    assert result == expected_result