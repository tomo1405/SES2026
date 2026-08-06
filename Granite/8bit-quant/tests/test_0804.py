import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src_0804 import task_func
import pytest

def test_task_func_with_numeric_columns():
    file_name = "test_data.csv"
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": [7, 8, 9]
    })
    df.to_csv(file_name, index=False)

    result = task_func(file_name)

    expected = pd.DataFrame({
        "A": [0.0, 0.5, 1.0],
        "B": [0.0, 0.5, 1.0],
        "C": [0.0, 0.5, 1.0]
    })

    assert result.equals(expected)

def test_task_func_with_non_numeric_columns():
    file_name = "test_data.csv"
    df = pd.DataFrame({
        "A": ["a", "b", "c"],
        "B": [4, 5, 6],
        "C": [7, 8, 9]
    })
    df.to_csv(file_name, index=False)

    with pytest.raises(ValueError) as excinfo:
        task_func(file_name)

    assert "Input must at least have one numeric column." in str(excinfo.value)

def test_task_func_with_empty_file():
    file_name = "test_data.csv"
    df = pd.DataFrame()
    df.to_csv(file_name, index=False)

    with pytest.raises(ValueError) as excinfo:
        task_func(file_name)

    assert "Input must at least have one numeric column." in str(excinfo.value)