import pytest
from src_0435 import task_func
import pandas as pd
import random

# Test cases for task_func

def test_task_func_basic():
    s = """1,234,10,5.50,Apple,Description1
2,345,20,6.00,Banana,Description2
3,567,30,7.50,Orange,Description3"""
    result = task_func(s)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert "ID" in result.columns
    assert "Quantity" in result.columns
    assert "Code" in result.columns
    assert "Price" in result.columns
    assert "Product" in result.columns
    assert "Description" in result.columns

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func("invalid input")

def test_task_func_random_product():
    s = """1,234,10,5.50,,Description1
2,345,20,6.00,Banana,Description2
3,567,30,7.50,Orange,Description3"""
    result = task_func(s)
    assert "Apple" in result["Product"].values