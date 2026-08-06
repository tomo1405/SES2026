import pytest
from src_0415 import task_func

def test_task_func_no_data():
    data = []
    df, ax = task_func(data)
    assert df.empty
    assert ax is None

def test_task_func_no_numeric_data():
    data = [{'a': 'text', 'b': 'more text'}]
    df, ax = task_func(data)
    assert df.empty
    assert ax is None

def test_task_func_drop_column():
    data = [{'a': 1, 'b': 2, 'c': 3}]
    df, ax = task_func(data, column='b')
    assert 'b' not in df.columns
    assert 'a' in df.columns
    assert 'c' in df.columns
    assert ax is not None

def test_task_func_default_column():
    data = [{'a': 1, 'b': 2, 'c': 3}]
    df, ax = task_func(data)
    assert 'c' not in df.columns
    assert 'a' in df.columns
    assert 'b' in df.columns
    assert ax is not None

def test_task_func_empty_dataframe_after_drop():
    data = [{'a': 1, 'b': 2, 'c': 3}]
    df, ax = task_func(data, column='a')
    assert df.empty
    assert ax is None

def test_task_func_with_non_numeric_column_to_drop():
    data = [{'a': 1, 'b': 'text', 'c': 3}]
    df, ax = task_func(data, column='b')
    assert 'b' not in df.columns
    assert 'a' in df.columns
    assert 'c' in df.columns
    assert ax is not None

def test_task_func_with_all_columns_numeric():
    data = [{'a': 1, 'b': 2, 'c': 3}]
    df, ax = task_func(data)
    assert 'c' not in df.columns
    assert 'a' in df.columns
    assert 'b' in df.columns
    assert ax is not None

def test_task_func_with_mixed_data_types():
    data = [{'a': 1, 'b': 'text', 'c': 3}, {'a': 4, 'b': 'more text', 'c': 5}]
    df, ax = task_func(data)
    assert 'c' not in df.columns
    assert 'a' in df.columns
    assert 'b' in df.columns
    assert ax is not None