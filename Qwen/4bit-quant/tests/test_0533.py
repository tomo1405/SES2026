import pytest
from src_0533 import task_func
import pandas as pd
import numpy as np
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        "value": [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    }
    return pd.DataFrame(data)

def test_task_func_with_duplicates(sample_df):
    duplicates_counter, ax = task_func(sample_df)
    assert isinstance(duplicates_counter, Counter)
    assert duplicates_counter == Counter({2: 2, 3: 3, 4: 4})
    assert isinstance(ax, plt.Axes)

def test_task_func_with_no_duplicates():
    data = {
        "value": [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    duplicates_counter, ax = task_func(df)
    assert isinstance(duplicates_counter, Counter)
    assert duplicates_counter == Counter()
    assert isinstance(ax, plt.Axes)

def test_task_func_with_empty_df():
    df = pd.DataFrame(columns=["value"])
    duplicates_counter, ax = task_func(df)
    assert isinstance(duplicates_counter, Counter)
    assert duplicates_counter == Counter()
    assert isinstance(ax, plt.Axes)

def test_task_func_with_constant_value():
    data = {
        "value": [5, 5, 5, 5, 5]
    }
    df = pd.DataFrame(data)
    duplicates_counter, ax = task_func(df)
    assert isinstance(duplicates_counter, Counter)
    assert duplicates_counter == Counter({5: 5})
    assert isinstance(ax, plt.Axes)

def test_task_func_with_bins_parameter():
    data = {
        "value": [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    }
    df = pd.DataFrame(data)
    duplicates_counter, ax = task_func(df, bins=5)
    assert isinstance(duplicates_counter, Counter)
    assert duplicates_counter == Counter({2: 2, 3: 3, 4: 4})
    assert isinstance(ax, plt.Axes)