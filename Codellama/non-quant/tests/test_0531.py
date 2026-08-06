import pytest
from src_0531 import task_func
import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func_empty_input():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_invalid_age():
    df = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "age": [-1, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_valid_input():
    df = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "age": [20, 30, 40]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert ax is None

def test_task_func_duplicate_names():
    df = pd.DataFrame({"name": ["Alice", "Bob", "Charlie", "Alice"], "age": [20, 30, 40, 50]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter({20: 1, 30: 1, 40: 1, 50: 1})
    assert ax is not None
    assert ax.get_xlabel() == "Age"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Distribution of Ages for Duplicate Names"