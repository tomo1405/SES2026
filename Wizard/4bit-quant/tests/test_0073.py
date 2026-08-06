python
import pandas as pd
import os
import numpy as np
import ast
import pytest

from src_0073 import task_func

def test_task_func():
    # Test case 1: Directory with no CSV files
    directory = "test_data/no_csv_files"
    df, hist = task_func(directory)
    assert df.empty
    assert hist is None

    # Test case 2: Directory with one CSV file
    directory = "test_data/one_csv_file"
    df, hist = task_func(directory)
    assert df.shape == (10, 6)
    assert hist is not None

    # Test case 3: Directory with multiple CSV files
    directory = "test_data/multiple_csv_files"
    df, hist = task_func(directory)
    assert df.shape == (30, 6)
    assert hist is not None