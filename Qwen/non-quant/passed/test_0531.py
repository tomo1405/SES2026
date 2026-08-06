import pytest
from src_0531 import task_func
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def test_task_func_empty_df():
    df = pd.DataFrame(columns=["name", "age"])
    with pytest.raises(ValueError, match="Input data cannot be empty."):
        task_func(df)

def test_task_func_invalid_age():
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [-1, 25]})
    with pytest.raises(ValueError, match="Invalid age: age cannot be less than 0."):
        task_func(df)

def test_task_func_no_duplicates():
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
    counter, ax = task_func(df)
    assert isinstance(counter, Counter)
    assert counter == Counter()
    assert ax is None

def test_task_func_with_duplicates():
    df = pd.DataFrame({"name": ["Alice", "Alice", "Bob", "Bob", "Bob"], "age": [25.5, 25.5, 30, 30, 35]})
    counter, ax = task_func(df)
    assert isinstance(counter, Counter)
    assert counter == Counter({25: 2, 30: 2})
    assert isinstance(ax, plt.Axes)

def test_task_func_flooring_of_ages():
    df = pd.DataFrame({"name": ["Alice", "Alice"], "age": [25.7, 25.2]})
    counter, ax = task_func(df)
    assert isinstance(counter, Counter)
    assert counter == Counter({25: 2})
    assert isinstance(ax, plt.Axes)

def test_task_func_single_duplicate():
    df = pd.DataFrame({"name": ["Alice", "Alice", "Bob"], "age": [25, 25, 30]})
    counter, ax = task_func(df)
    assert isinstance(counter, Counter)
    assert counter == Counter({25: 2})
    assert isinstance(ax, plt.Axes)