import pytest
from src_0838 import task_func

def test_task_func():
    # Test case 1: Test with default arguments
    n_rows = 100
    scale_cols = [0, 2, 4]
    expected_result = task_func(n_rows, scale_cols)
    assert isinstance(expected_result, pd.DataFrame)
    assert expected_result.shape == (n_rows, 5)
    
    # Test case 2: Test with custom arguments
    n_rows = 50
    scale_cols = [1, 3]
    columns = ['X', 'Y', 'Z']
    random_seed = 42
    expected_result = task_func(n_rows, scale_cols, columns=columns, random_seed=random_seed)
    assert isinstance(expected_result, pd.DataFrame)
    assert expected_result.shape == (n_rows, 3)
    assert expected_result.columns.tolist() == columns