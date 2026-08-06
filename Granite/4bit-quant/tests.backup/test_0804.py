import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src_0804 import task_func
import pytest

def test_task_func_with_valid_input():
    file_name = "valid_input.csv"
    expected_output = pd.DataFrame({
        "A": [0, 1],
        "B": [0, 1]
    })
    df = task_func(file_name)
    assert df.equals(expected_output)

def test_task_func_with_invalid_input():
    file_name = "invalid_input.csv"
    with pytest.raises(ValueError) as exc_info:
        task_func(file_name)
    assert "Input must at least have one numeric column." in str(exc_info.value)

def test_task_func_with_min_max_scaler():
    file_name = "valid_input.csv"
    df = pd.DataFrame({
        "A": [1, 2],
        "B": [3, 4]
    })
    expected_output = pd.DataFrame({
        "A": [0, 1],
        "B": [0, 1]
    })
    df = task_func(file_name)
    assert df.equals(expected_output)