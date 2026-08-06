import collections

from src_0389 import task_func


def test_task_func():
    my_tuple = ('column1', 'column2', 'column3')
    path_csv_files = ['path/to/file1.csv', 'path/to/file2.csv']
    expected_output = {
        'column1': collections.Counter({'value1': 10, 'value2': 5}),
        'column2': collections.Counter({'value3': 8, 'value4': 3}),
        'column3': collections.Counter({'value5': 12, 'value6': 7})
    }

    actual_output = task_func(my_tuple, path_csv_files)

    assert actual_output == expected_output