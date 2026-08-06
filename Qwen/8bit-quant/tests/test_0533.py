import pytest
from src_0533 import task_func
import pandas as pd
import numpy as np
from collections import Counter

def test_task_func_empty_df():
    df = pd.DataFrame(columns=["value"])
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

def test_task_func_constant_df():
    df = pd.DataFrame({"value": [1, 1, 1]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter({1: 3})
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

def test_task_func_no_duplicates():
    df = pd.DataFrame({"value": [1, 2, 3, 4]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

def test_task_func_with_duplicates():
    df = pd.DataFrame({"value": [1, 2, 2, 3, 3, 3]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter({2: 2, 3: 3})
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

def test_task_func_normal_distribution():
    np.random.seed(0)
    data = np.random.normal(loc=0, scale=1, size=1000)
    df = pd.DataFrame({"value": data})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"