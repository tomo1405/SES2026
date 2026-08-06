import pandas as pd
from src_0317 import task_func


def test_task_func_return_type():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The function should return a pandas DataFrame"

def test_task_func_columns():
    result = task_func()
    expected_columns = ['Category', 'Count']
    assert list(result.columns) == expected_columns, "DataFrame should have columns 'Category' and 'Count'"

def test_task_func_category_values():
    result = task_func()
    assert all(category in CATEGORIES for category in result['Category']), "All categories should be in the predefined CATEGORIES list"

def test_task_func_count_values():
    result = task_func()
    assert all(isinstance(count, int) for count in result['Count']), "All counts should be integers"

def test_task_func_value_range():
    value_range = (10, 20)
    result = task_func(value_range=value_range)
    assert all(count >= value_range[0] and count <= value_range[1] for count in result['Count']), "Counts should be within the specified value range"

def test_task_func_default_value_range():
    result = task_func()
    default_value_range = (0, 100)
    assert all(count >= default_value_range[0] and count <= default_value_range[1] for count in result['Count']), "Counts should be within the default value range when no range is specified"