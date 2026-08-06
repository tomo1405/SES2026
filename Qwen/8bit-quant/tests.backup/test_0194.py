import pytest
from src_0194 import task_func
import pandas as pd

def test_task_func_output_type():
    df = task_func(5, 3)
    assert isinstance(df, pd.DataFrame)

def test_task_func_column_count():
    df = task_func(5, 3)
    assert len(df.columns) == 3

def test_task_func_row_count():
    df = task_func(5, 3)
    assert len(df) == 5

def test_task_func_column_data_types():
    df = task_func(5, 3)
    for col in df.columns:
        col_data = df[col].tolist()
        unique_types = {type(item) for item in col_data}
        assert len(unique_types) == 1, f"Column {col} contains multiple data types"

def test_task_func_randomness():
    df1 = task_func(5, 3)
    df2 = task_func(5, 3)
    assert not df1.equals(df2), "Two calls to task_func should produce different DataFrames"

def test_task_func_empty_df():
    with pytest.raises(ValueError):
        task_func(0, 3)

def test_task_func_zero_columns():
    df = task_func(5, 0)
    assert df.empty

def test_task_func_negative_rows():
    with pytest.raises(ValueError):
        task_func(-1, 3)

def test_task_func_negative_columns():
    with pytest.raises(ValueError):
        task_func(5, -1)