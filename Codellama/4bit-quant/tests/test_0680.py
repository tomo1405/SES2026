import pandas as pd
from src_0680 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected_result = {(1, 4): 1, (2, 5): 1, (3, 6): 1}
    assert task_func(df) == expected_result

def test_task_func_with_duplicates():
    df = pd.DataFrame({'A': [1, 2, 3, 1], 'B': [4, 5, 6, 4]})
    expected_result = {(1, 4): 2, (2, 5): 1, (3, 6): 1}
    assert task_func(df) == expected_result

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    expected_result = {}
    assert task_func(df) == expected_result