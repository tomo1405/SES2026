import pandas as pd
from src_0800 import task_func


def test_task_func_empty_list():
    L = []
    num_dataframes = 5
    random_seed = None
    expected_common_rows = pd.DataFrame()
    expected_dataframes = []

    common_rows, dataframes = task_func(L, num_dataframes, random_seed)

    assert common_rows.equals(expected_common_rows)
    assert dataframes == expected_dataframes

def test_task_func_non_empty_list():
    L = ['a', 'b', 'c', 'd', 'e']
    num_dataframes = 5
    random_seed = None
    expected_common_rows = pd.DataFrame()
    expected_dataframes = []

    common_rows, dataframes = task_func(L, num_dataframes, random_seed)

    assert common_rows.equals(expected_common_rows)
    assert dataframes == expected_dataframes

def test_task_func_random_seed():
    L = ['a', 'b', 'c', 'd', 'e']
    num_dataframes = 5
    random_seed = 1234
    expected_common_rows = pd.DataFrame()
    expected_dataframes = []

    common_rows, dataframes = task_func(L, num_dataframes, random_seed)

    assert common_rows.equals(expected_common_rows)
    assert dataframes == expected_dataframes

def test_task_func_num_dataframes():
    L = ['a', 'b', 'c', 'd', 'e']
    num_dataframes = 10
    random_seed = None
    expected_common_rows = pd.DataFrame()
    expected_dataframes = []

    common_rows, dataframes = task_func(L, num_dataframes, random_seed)

    assert common_rows.equals(expected_common_rows)
    assert dataframes == expected_dataframes