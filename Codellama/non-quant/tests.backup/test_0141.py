import pytest
from src_0141 import task_func

def test_task_func_input_df_not_dataframe():
    df = "not a dataframe"
    cols = ["col1", "col2"]
    with pytest.raises(ValueError):
        task_func(df, cols)

def test_task_func_input_cols_not_list():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    cols = "not a list"
    with pytest.raises(ValueError):
        task_func(df, cols)

def test_task_func_input_cols_not_all_str():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    cols = [1, 2]
    with pytest.raises(ValueError):
        task_func(df, cols)

def test_task_func_input_cols_not_all_in_df():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    cols = ["col1", "col3"]
    with pytest.raises(ValueError):
        task_func(df, cols)

def test_task_func_output_df_scaled():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    cols = ["col1", "col2"]
    df_scaled = task_func(df, cols)
    assert df_scaled.equals(pd.DataFrame({"col1": [-1.0, 0.0, 1.0], "col2": [-1.0, 0.0, 1.0]}))