import pytest
from src_0496 import task_func

def test_task_func_output_type():
    df = task_func(5)
    assert isinstance(df, pd.DataFrame), "The output should be a pandas DataFrame"

def test_task_func_index():
    df = task_func(5)
    assert all(isinstance(index, pd.Timestamp) for index in df.index), "Index should be of type pd.Timestamp"

def test_task_func_columns():
    df = task_func(5)
    expected_columns = ["Groceries", "Entertainment", "Rent", "Utilities", "Miscellaneous"]
    assert list(df.columns) == expected_columns, "DataFrame should have the correct columns"

def test_task_func_random_values():
    df1 = task_func(5, random_seed=0)
    df2 = task_func(5, random_seed=0)
    assert df1.equals(df2), "DataFrame should produce the same values with the same random seed"

def test_task_func_different_random_seeds():
    df1 = task_func(5, random_seed=0)
    df2 = task_func(5, random_seed=1)
    assert not df1.equals(df2), "DataFrame should produce different values with different random seeds"

def test_task_func_correct_number_of_days():
    days = 10
    df = task_func(days)
    assert len(df) == days, "DataFrame should have the correct number of rows based on the input days"