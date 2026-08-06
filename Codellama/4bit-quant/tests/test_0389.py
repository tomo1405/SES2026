import collections

from src_0389 import task_func


def test_task_func():
    my_tuple = ('a', 'b', 'c')
    path_csv_files = ['file1.csv', 'file2.csv']
    expected_counter = {'a': collections.Counter({'x': 2, 'y': 3}),
                        'b': collections.Counter({'x': 1, 'y': 2}),
                        'c': collections.Counter({'x': 1, 'y': 1})}

    counter = task_func(my_tuple, path_csv_files)

    assert counter == expected_counter