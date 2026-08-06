import pytest
from src_1060 import task_func
import pandas as pd
import numpy as np

def test_task_func_output_shape():
    df = task_func()
    assert df.shape == (len(PLANETS), len(ELEMENTS)), "DataFrame shape is incorrect"

def test_task_func_columns():
    df = task_func()
    assert list(df.columns) == ELEMENTS, "Column headers do not match ELEMENTS"

def test_task_func_unique_pairs():
    df = task_func()
    unique_pairs = set(df.values.flatten())
    expected_pairs = {f"{planet}:{element}" for planet in PLANETS for element in ELEMENTS}
    assert unique_pairs == expected_pairs, "Not all pairs are present or there are duplicates"

def test_task_func_randomness():
    df1 = task_func()
    df2 = task_func()
    assert not df1.equals(df2), "The DataFrames are identical, indicating lack of randomness"

def test_task_func_data_types():
    df = task_func()
    assert isinstance(df, pd.DataFrame), "Return type is not a DataFrame"
    assert df.dtypes.apply(lambda x: x == object).all(), "All elements in the DataFrame should be strings"