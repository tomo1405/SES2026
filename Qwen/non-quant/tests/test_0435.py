import pandas as pd
import pytest
from src_0435 import task_func


def test_task_func_with_valid_input():
    input_data = """1 10 A1 100 Apple
2 20 B2 200 Banana
3 30 C3 300 Orange"""
    expected_output = pd.DataFrame({
        "ID": [1, 2, 3],
        "Quantity": [10, 20, 30],
        "Code": ["A1", "B2", "C3"],
        "Price": [100, 200, 300],
        "Product": ["Apple", "Banana", "Orange"],
        "Description": [None, None, None]
    })
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_missing_product_code():
    input_data = """1 10 A1 100
2 20 B2 200 Banana
3 30 C3 300 Orange"""
    expected_output = pd.DataFrame({
        "ID": [1, 2, 3],
        "Quantity": [10, 20, 30],
        "Code": ["A1", "B2", "C3"],
        "Price": [100, 200, 300],
        "Product": ["Apple", "Banana", "Orange"],
        "Description": [None, None, None]
    })
    result = task_func(input_data, seed=42)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_empty_input():
    with pytest.raises(ValueError, match="Incomplete data provided."):
        task_func("")

def test_task_func_with_incomplete_segment():
    with pytest.raises(ValueError, match="Incomplete data provided."):
        task_func("1 10 A1 100")

def test_task_func_with_random_product_assignment():
    input_data = """1 10 X1 100
2 20 Y2 200
3 30 Z3 300"""
    expected_products = ["Apple", "Banana", "Orange", "Pear", "Grape"]
    result = task_func(input_data, seed=42)
    assert all(product in expected_products for product in result["Product"])

def test_task_func_with_random_seed_consistency():
    input_data = """1 10 X1 100
2 20 Y2 200
3 30 Z3 300"""
    result1 = task_func(input_data, seed=42)
    result2 = task_func(input_data, seed=42)
    pd.testing.assert_frame_equal(result1, result2)