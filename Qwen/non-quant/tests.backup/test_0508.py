import pytest
from src_0508 import task_func

def test_task_func_invalid_column():
    with pytest.raises(ValueError, match="Invalid column name."):
        task_func("InvalidColumn", [])

def test_task_func_invalid_data_type():
    with pytest.raises(ValueError, match="Data must be a list of lists"):
        task_func("Open", "not a list")

def test_task_func_invalid_inner_list_length():
    with pytest.raises(ValueError, match="Data must be a list of lists"):
        task_func("Open", [[1, 2], [3, 4, 5]])

def test_task_func_empty_data():
    result = task_func("Open", [])
    assert result == {"sum": 0, "mean": float("nan"), "min": float("nan"), "max": float("nan")}

def test_task_func_single_row_data():
    data = [[1, 2, 3, 4, 5, 6]]
    result = task_func("Open", data)
    assert result == {"sum": 1, "mean": 1.0, "min": 1, "max": 1}

def test_task_func_multiple_rows_data():
    data = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]
    ]
    result = task_func("Open", data)
    assert result == {"sum": 31, "mean": 10.333333333333334, "min": 1, "max": 13}

def test_task_func_all_nan_values():
    data = [
        [np.nan, 2, 3, 4, 5, 6],
        [np.nan, 8, 9, 10, 11, 12],
        [np.nan, 14, 15, 16, 17, 18]
    ]
    result = task_func("Open", data)
    assert result == {"sum": 0, "mean": float("nan"), "min": float("nan"), "max": float("nan")}