import pandas as pd
from random import seed, choices
from src_0800 import task_func

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_common_rows = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_dataframes = [pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])]

    common_rows, dataframes = task_func(L)

    assert common_rows.equals(expected_common_rows)
    assert dataframes == expected_dataframes

def test_task_func_with_seed():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    random_seed = 42
    seed(random_seed)
    expected_common_rows = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_dataframes = [pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])]

    common_rows, dataframes = task_func(L, random_seed=random_seed)

    assert common_rows.equals(expected_common_rows)
    assert dataframes == expected_dataframes

def test_task_func_with_empty_list():
    L = []
    expected_common_rows = pd.DataFrame()
    expected_dataframes = []

    common_rows, dataframes = task_func(L)

    assert common_rows.equals(expected_common_rows)
    assert dataframes == expected_dataframes