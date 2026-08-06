import pytest
from src_0322 import task_func
import pandas as pd
import re
from scipy import stats
import matplotlib.pyplot as plt

# Mocking the plot method to avoid creating actual plots during testing
class MockAxes:
    def __init__(self):
        pass

    def set_title(self, title):
        pass

@pytest.fixture
def mock_plot(monkeypatch):
    def mock_bar(*args, **kwargs):
        return MockAxes()

    monkeypatch.setattr(pd.Series, 'plot', mock_bar)

def test_task_func_no_names():
    text = "No names here"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.empty
    assert ax is None
    assert skewness is None
    assert kurtosis is None

def test_task_func_single_name():
    text = "Alice"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs['Alice'] == 1
    assert isinstance(ax, MockAxes)
    assert skewness is not None
    assert kurtosis is not None

def test_task_func_multiple_names():
    text = "Alice [extra info] Bob Charlie Alice"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs['Alice'] == 2
    assert name_freqs['Bob'] == 1
    assert name_freqs['Charlie'] == 1
    assert isinstance(ax, MockAxes)
    assert skewness is not None
    assert kurtosis is not None

def test_task_func_empty_string():
    text = ""
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.empty
    assert ax is None
    assert skewness is None
    assert kurtosis is None

def test_task_func_whitespace():
    text = "   "
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.empty
    assert ax is None
    assert skewness is None
    assert kurtosis is None

def test_task_func_with_brackets():
    text = "Alice [extra info]"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs['Alice'] == 1
    assert isinstance(ax, MockAxes)
    assert skewness is not None
    assert kurtosis is not None

def test_task_func_with_multiple_brackets():
    text = "Alice [extra info] Bob [more info] Charlie"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs['Alice'] == 1
    assert name_freqs['Bob'] == 1
    assert name_freqs['Charlie'] == 1
    assert isinstance(ax, MockAxes)
    assert skewness is not None
    assert kurtosis is not None