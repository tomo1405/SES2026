import pandas as pd
from sklearn.preprocessing import StandardScaler
from src_0141 import task_func
import pytest

def test_task_func_input_df():
    with pytest.raises(ValueError) as excinfo:
        task_func("not_a_df", ["col1", "col2"])
    assert "The input df must be a pandas DataFrame." in str(excinfo.value)

def test_task_func_cols():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    with pytest.raises(ValueError) as excinfo:
        task_func(df, "not_a_list")
    assert "cols must be a list of column names." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        task_func(df, ["col1", 2])
    assert "All columns in cols must exist in the dataframe." in str(excinfo.value)

def test_task_func_scaling():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    scaled_df = task_func(df, ["col1", "col2"])
    scaler = StandardScaler()
    expected_result = pd.DataFrame(scaler.fit_transform(df[["col1", "col2"]]), columns=["col1", "col2"])
    assert scaled_df.equals(expected_result)