import pytest
from src_0496 import task_func

def test_task_func():
    days = 10
    random_seed = 0
    df = task_func(days, random_seed)
    assert df.shape == (days, 5)
    assert df.columns.tolist() == ["date", "Groceries", "Entertainment", "Rent", "Utilities", "Miscellaneous"]
    assert df.index.name == "date"
    assert df.index.dtype == "datetime64[ns]"
    assert df.dtypes.tolist() == ["datetime64[ns]", "int64", "int64", "int64", "int64", "int64"]
    assert df.sum().tolist() == [0, 0, 0, 0, 0, 0]

def test_task_func_with_different_random_seed():
    days = 10
    random_seed = 1
    df = task_func(days, random_seed)
    assert df.shape == (days, 5)
    assert df.columns.tolist() == ["date", "Groceries", "Entertainment", "Rent", "Utilities", "Miscellaneous"]
    assert df.index.name == "date"
    assert df.index.dtype == "datetime64[ns]"
    assert df.dtypes.tolist() == ["datetime64[ns]", "int64", "int64", "int64", "int64", "int64"]
    assert df.sum().tolist() == [0, 0, 0, 0, 0, 0]

def test_task_func_with_different_days():
    days = 20
    random_seed = 0
    df = task_func(days, random_seed)
    assert df.shape == (days, 5)
    assert df.columns.tolist() == ["date", "Groceries", "Entertainment", "Rent", "Utilities", "Miscellaneous"]
    assert df.index.name == "date"
    assert df.index.dtype == "datetime64[ns]"
    assert df.dtypes.tolist() == ["datetime64[ns]", "int64", "int64", "int64", "int64", "int64"]
    assert df.sum().tolist() == [0, 0, 0, 0, 0, 0]