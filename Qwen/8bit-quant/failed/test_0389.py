import pytest
from src_0389 import task_func
import pandas as pd
import os

@pytest.fixture
def setup_test_data(tmpdir):
    # Create temporary CSV files for testing
    file1 = tmpdir.join("file1.csv")
    file2 = tmpdir.join("file2.csv")

    data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    data2 = {'A': [1, 2, 2], 'B': [4, 5, 5]}

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    df1.to_csv(file1, index=False)
    df2.to_csv(file2, index=False)

    return [str(file1), str(file2)]

def test_task_func(setup_test_data):
    my_tuple = ('A', 'B')
    path_csv_files = setup_test_data

    result = task_func(my_tuple, path_csv_files)

    expected_result = {
        'A': collections.Counter({1: 2, 2: 3, 3: 1}),
        'B': collections.Counter({4: 2, 5: 3, 6: 1})
    }

    assert result == expected_result

def test_task_func_missing_column(setup_test_data):
    my_tuple = ('A', 'C')
    path_csv_files = setup_test_data

    result = task_func(my_tuple, path_csv_files)

    expected_result = {
        'A': collections.Counter({1: 2, 2: 3, 3: 1}),
        'C': collections.Counter()
    }

    assert result == expected_result

def test_task_func_empty_files(setup_test_data):
    my_tuple = ('A', 'B')
    path_csv_files = setup_test_data

    # Create empty files
    open(path_csv_files[0], 'w').close()
    open(path_csv_files[1], 'w').close()

    result = task_func(my_tuple, path_csv_files)

    expected_result = {
        'A': collections.Counter(),
        'B': collections.Counter()
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