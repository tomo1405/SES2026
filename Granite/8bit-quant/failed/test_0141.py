import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0141 import task_func

def test_task_func_input_df_type():
    with pytest.raises(ValueError) as excinfo:
        task_func(123, ["col1", "col2"])
    assert "The input df must be a pandas DataFrame." in str(excinfo.value)

def test_task_func_cols_type():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    with pytest.raises(ValueError) as excinfo:
        task_func(df, 123)
    assert "cols must be a list of column names." in str(excinfo.value)

def test_task_func_cols_content():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    with pytest.raises(ValueError) as excinfo:
        task_func(df, ["col1", 123])
    assert "All columns in cols must exist in the dataframe." in str(excinfo.value)

def test_task_func_scaling():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    cols = ["col1", "col2"]
    expected_result = pd.DataFrame({
        "col1": [-1.22474487, -0.69096331, 0.69096331],
        "col2": [-1.22474487, -0.69096331, 0.69096331]
    })
    result = task_func(df, cols)
    assert result.equals(expected_result)