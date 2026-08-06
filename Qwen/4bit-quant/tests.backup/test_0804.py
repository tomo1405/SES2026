import pytest
from src_0804 import task_func
import pandas as pd

# Mocking the pandas read_csv function to simulate file reading
def mock_read_csv(file_name):
    if file_name == "valid_data.csv":
        return pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4.0, 5.0, 6.0]
        })
    elif file_name == "no_numeric_data.csv":
        return pd.DataFrame({
            'C': ['a', 'b', 'c'],
            'D': ['d', 'e', 'f']
        })
    else:
        raise FileNotFoundError(f"No such file: {file_name}")

@pytest.fixture(autouse=True)
def patch_read_csv(monkeypatch):
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

def test_task_func_valid_data():
    result_df = task_func("valid_data.csv")
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.shape == (3, 2)
    assert all(result_df['A'] >= 0) and all(result_df['A'] <= 1)
    assert all(result_df['B'] >= 0) and all(result_df['B'] <= 1)

def test_task_func_no_numeric_data():
    with pytest.raises(ValueError, match="Input must at least have one numeric column."):
        task_func("no_numeric_data.csv")

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError, match="No such file: non_existent_file.csv"):
        task_func("non_existent_file.csv")