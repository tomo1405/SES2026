import pytest
from src_0322 import task_func
import pandas as pd
import numpy as np
from scipy import stats

def test_task_func_no_names():
    text = "No names here"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.empty
    assert ax is None
    assert skewness is None
    assert kurtosis is None

def test_task_func_single_name():
    text = "Alice [some info]"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    expected_freqs = pd.Series({'Alice': 1})
    pd.testing.assert_series_equal(name_freqs, expected_freqs)
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None

def test_task_func_multiple_names():
    text = "Alice [info] Bob [info] Alice [info]"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    expected_freqs = pd.Series({'Alice': 2, 'Bob': 1})
    pd.testing.assert_series_equal(name_freqs, expected_freqs)
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None

def test_task_func_empty_names():
    text = "[info] [info]"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.empty
    assert ax is None
    assert skewness is None
    assert kurtosis is None

def test_task_func_whitespace_names():
    text = "   [info] \t [info] "
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.empty
    assert ax is None
    assert skewness is None
    assert kurtosis is None