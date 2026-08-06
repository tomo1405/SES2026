import pytest
from src_1087 import task_func
import pandas as pd
import numpy as np

def test_task_func_output_type():
    df = task_func()
    assert isinstance(df, pd.DataFrame), "The function should return a pandas DataFrame."

def test_task_func_number_of_rows():
    df = task_func()
    assert len(df) == 1000, "The DataFrame should have 1000 rows."

def test_task_func_columns():
    df = task_func()
    expected_columns = ["String Field", "Float Field"]
    assert list(df.columns) == expected_columns, "The DataFrame should have the correct columns."

def test_task_func_string_field_length():
    df = task_func()
    for value in df["String Field"]:
        assert len(value) == 10, "Each entry in 'String Field' should be 10 characters long."

def test_task_func_float_field_format():
    df = task_func()
    for value in df["Float Field"]:
        try:
            float(value.replace(",", ""))
        except ValueError:
            pytest.fail("Each entry in 'Float Field' should be a formatted float.")

def test_task_func_float_field_range():
    df = task_func()
    for value in df["Float Field"]:
        numeric_value = float(value.replace(",", ""))
        assert 0 <= numeric_value <= 10000, "Each entry in 'Float Field' should be between 0 and 10000."