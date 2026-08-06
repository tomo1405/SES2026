import collections

import pandas as pd
import pytest
from src_0389 import task_func


@pytest.fixture
def create_temp_csv_files(tmpdir):
    # Create temporary CSV files with sample data
    file1_path = tmpdir.join("file1.csv")
    file2_path = tmpdir.join("file2.csv")

    data1 = {'A': [1, 2, 3], 'B': ['a', 'b', 'c']}
    data2 = {'A': [4, 5, 6], 'B': ['d', 'e', 'f']}

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    df1.to_csv(file1_path, index=False)
    df2.to_csv(file2_path, index=False)

    return [str(file1_path), str(file2_path)]

def test_task_func(create_temp_csv_files):
    my_tuple = ('A', 'B')
    path_csv_files = create_temp_csv_files

    result = task_func(my_tuple, path_csv_files)

    expected_result = {
        'A': collections.Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}),
        'B': collections.Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1})
    }

    assert result == expected_result

def test_task_func_with_missing_column(create_temp_csv_files):
    my_tuple = ('A', 'C')
    path_csv_files = create_temp_csv_files

    result = task_func(my_tuple, path_csv_files)

    expected_result = {
        'A': collections.Counter({1: 1, 2: 1, 3: 1, 4: 5, 5: 5, 6: 5}),
        'C': collections.Counter()
    }

    assert result == expected_result

def test_task_func_empty_csv(create_temp_csv_files):
    my_tuple = ('A', 'B')
    path_csv_files = [create_temp_csv_files[0], create_temp_csv_files[0]]  # Duplicate the same file

    result = task_func(my_tuple, path_csv_files)

    expected_result = {
        'A': collections.Counter({1: 2, 2: 2, 3: 2}),
        'B': collections.Counter({'a': 2, 'b': 2, 'c': 2})
    }

    assert result == expected_result

def test_task_func_no_files():
    my_tuple = ('A', 'B')
    path_csv_files = []

    result = task_func(my_tuple, path_csv_files)

    expected_result = {
        'A': collections.Counter(),
        'B': collections.Counter()
    }

    assert result == expected_result