import pytest
from src_0533 import task_func
import pandas as pd
import numpy as np
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Mocking matplotlib to capture plot output
class MockAxes:
    def hist(self, *args, **kwargs):
        pass

    def plot(self, *args, **kwargs):
        pass

    def set_xlabel(self, label):
        pass

    def set_ylabel(self, label):
        pass

    def set_title(self, title):
        pass

    def get_figure(self):
        return MockFigure()

class MockFigure:
    def savefig(self, *args, **kwargs):
        pass

@pytest.fixture
def mock_plt(monkeypatch):
    monkeypatch.setattr(plt, 'subplots', lambda: (MockFigure(), MockAxes()))

def test_task_func_empty_df(mock_plt):
    df = pd.DataFrame(columns=["value"])
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert isinstance(ax, MockAxes)

def test_task_func_constant_df(mock_plt):
    df = pd.DataFrame({"value": [1, 1, 1]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter({1: 3})
    assert isinstance(ax, MockAxes)

def test_task_func_no_duplicates(mock_plt):
    df = pd.DataFrame({"value": [1, 2, 3, 4]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert isinstance(ax, MockAxes)

def test_task_func_with_duplicates(mock_plt):
    df = pd.DataFrame({"value": [1, 2, 2, 3, 3, 3, 4]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter({2: 2, 3: 3})
    assert isinstance(ax, MockAxes)

def test_task_func_normal_distribution(mock_plt):
    np.random.seed(0)
    data = np.random.normal(loc=0, scale=1, size=1000)
    df = pd.DataFrame({"value": data})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert isinstance(ax, MockAxes)

def test_task_func_with_bins(mock_plt):
    df = pd.DataFrame({"value": [1, 2, 3, 4]})
    duplicates_counter, ax = task_func(df, bins=5)
    assert duplicates_counter == Counter()
    assert isinstance(ax, MockAxes)