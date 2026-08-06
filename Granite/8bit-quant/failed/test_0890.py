import os
import pandas as pd
import numpy as np
from src_0890 import task_func
import pytest

@pytest.fixture
def data_dir():
    return "path/to/data/dir"

@pytest.fixture
def csv_file():
    return "data.csv"

def test_task_func_with_numeric_columns(data_dir, csv_file):
    df = pd.DataFrame({
        "A": [1, 2, np.nan, 4],
        "B": [5, 6, 7, 8],
        "C": [9, 10, 11, 12]
    })
    df.to_csv(os.path.join(data_dir, csv_file), index=False)
    result = task_func(data_dir, csv_file)
    expected = pd.DataFrame({
        "A": [1, 2, 3, 4],
        "B": [5, 6, 7, 8],
        "C": [9, 10, 11, 12]
    })
    assert result.equals(expected)

def test_task_func_with_empty_data(data_dir, csv_file):
    df = pd.DataFrame()
    df.to_csv(os.path.join(data_dir, csv_file), index=False)
    result = task_func(data_dir, csv_file)
    expected = pd.DataFrame()
    assert result.equals(expected)

def test_task_func_with_non_numeric_columns(data_dir, csv_file):
    df = pd.DataFrame({
        "A": ["a", "b", "c", "d"],
        "B": [1, 2, 3, 4],
        "C": [5, 6, 7, 8]
    })
    df.to_csv(os.path.join(data_dir, csv_file), index=False)
    result = task_func(data_dir, csv_file)
    expected = pd.DataFrame({
        "A": ["a", "b", "c", "d"],
        "B": [1, 2, 3, 4],
        "C": [5, 6, 7, 8]
    })
    assert result.equals(expected)