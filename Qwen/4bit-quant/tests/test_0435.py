import pandas as pd
import pytest
from src_0435 import task_func


def test_task_func_with_valid_input():
    input_data = """
    1 10 A1 100 Apple
    2 20 B2 200 Banana
    3 30 C3 300 Orange
    """
    expected_output = pd.DataFrame({
        "ID": [1, 2, 3],
        "Quantity": [10, 20, 30],
        "Code": ["A1", "B2", "C3"],
        "Price": [100, 200, 300],
        "Product": ["Apple", "Banana", "Orange"],
        "Description": ["Apple", "Banana", "Orange"]
    })
    result = task_func(input_data, seed=42)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_missing_data():
    input_data = """
    1 10 A1 100 Apple
    2 20 B2 200 Banana
    """
    with pytest.raises(ValueError, match="Incomplete data provided."):
        task_func(input_data, seed=42)

def test_task_func_with_invalid_code():
    input_data = """
    1 10 X1 100 Apple
    2 20 B2 200 Banana
    """
    expected_output = pd.DataFrame({
        "ID": [1, 2],
        "Quantity": [10, 20],
        "Code": ["X1", "B2"],
        "Price": [100, 200],
        "Product": ["Grape", "Banana"],  # Assuming "Grape" is randomly chosen
        "Description": ["Apple", "Banana"]
    })
    result = task_func(input_data, seed=42)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_empty_string():
    with pytest.raises(ValueError, match="Incomplete data provided."):
        task_func("", seed=42)

def test_task_func_with_whitespace_only():
    with pytest.raises(ValueError, match="Incomplete data provided."):
        task_func("   ", seed=42)