import pytest
from src_0322 import task_func
import pandas as pd
import re
from scipy import stats

def test_task_func_no_names():
    text = "No names here!"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.empty
    assert ax is None
    assert skewness is None
    assert kurtosis is None

def test_task_func_single_name():
    text = "John Doe"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    expected_freqs = pd.Series({'John Doe': 1})
    assert name_freqs.equals(expected_freqs)
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None

def test_task_func_multiple_names():
    text = "John Doe [Manager], Jane Smith [Developer], John Doe [Designer]"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    expected_freqs = pd.Series({'John Doe': 2, 'Jane Smith': 1})
    assert name_freqs.equals(expected_freqs)
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None

def test_task_func_empty_string():
    text = ""
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.empty
    assert ax is None
    assert skewness is None
    assert kurtosis is None

def test_task_func_only_whitespace():
    text = "   "
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.empty
    assert ax is None
    assert skewness is None
    assert kurtosis is None

def test_task_func_special_characters():
    text = "John@Doe! Jane#Smith$"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    expected_freqs = pd.Series({'John@Doe!': 1, 'Jane#Smith$': 1})
    assert name_freqs.equals(expected_freqs)
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None