import random

import pandas as pd
from src_0317 import task_func


def test_task_func_output_type():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a pandas DataFrame"

def test_task_func_columns():
    result = task_func()
    assert list(result.columns) == ['Category', 'Count'], "DataFrame should have columns 'Category' and 'Count'"

def test_task_func_category_values():
    result = task_func()
    assert set(result['Category']) == set(CATEGORIES), "DataFrame should contain all categories from CATEGORIES"

def test_task_func_count_values():
    result = task_func()
    for count in result['Count']:
        assert isinstance(count, int), "Count values should be integers"
        assert 0 <= count <= 100, "Count values should be within the range 0 to 100"

def test_task_func_default_value_range():
    result = task_func()
    for count in result['Count']:
        assert 0 <= count <= 100, "Default value range should be 0 to 100"

def test_task_func_custom_value_range():
    result = task_func((50, 150))
    for count in result['Count']:
        assert 50 <= count <= 150, "Custom value range should be 50 to 150"

def test_task_func_reproducibility():
    random.seed(0)
    result1 = task_func()
    random.seed(0)
    result2 = task_func()
    assert result1.equals(result2), "Function should produce the same output with the same seed"