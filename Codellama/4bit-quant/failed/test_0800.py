import pytest
from src_0800 import task_func

def test_task_func():
    # Test case 1: Empty list
    L = []
    num_dataframes = 5
    random_seed = None
    expected_common_rows = pd.DataFrame()
    expected_dataframes = []
    actual_common_rows, actual_dataframes = task_func(L, num_dataframes, random_seed)
    assert actual_common_rows.equals(expected_common_rows)
    assert actual_dataframes == expected_dataframes

    # Test case 2: Non-empty list
    L = ['a', 'b', 'c']
    num_dataframes = 3
    random_seed = 123
    expected_common_rows = pd.DataFrame([['a', 'b', 'c']])
    expected_dataframes = [pd.DataFrame([['a', 'b', 'c']]), pd.DataFrame([['a', 'b', 'c']]), pd.DataFrame([['a', 'b', 'c']])]
    actual_common_rows, actual_dataframes = task_func(L, num_dataframes, random_seed)
    assert actual_common_rows.equals(expected_common_rows)
    assert actual_dataframes == expected_dataframes

    # Test case 3: Non-empty list with different lengths
    L = ['a', 'b', 'c', 'd', 'e']
    num_dataframes = 2
    random_seed = 456
    expected_common_rows = pd.DataFrame([['a', 'b', 'c']])
    expected_dataframes = [pd.DataFrame([['a', 'b', 'c']]), pd.DataFrame([['a', 'b', 'c']])]
    actual_common_rows, actual_dataframes = task_func(L, num_dataframes, random_seed)
    assert actual_common_rows.equals(expected_common_rows)
    assert actual_dataframes == expected_dataframes

    # Test case 4: Non-empty list with different lengths and different random seeds
    L = ['a', 'b', 'c', 'd', 'e']
    num_dataframes = 3
    random_seed = 789
    expected_common_rows = pd.DataFrame([['a', 'b', 'c']])
    expected_dataframes = [pd.DataFrame([['a', 'b', 'c']]), pd.DataFrame([['a', 'b', 'c']]), pd.DataFrame([['a', 'b', 'c']])]
    actual_common_rows, actual_dataframes = task_func(L, num_dataframes, random_seed)
    assert actual_common_rows.equals(expected_common_rows)
    assert actual_dataframes == expected_dataframes