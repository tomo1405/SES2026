import pytest
from src_0525 import task_func
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

# Mocking plt.subplots to capture calls
class MockSubplots:
    def __init__(self):
        self.ax = MockAx()

    def subplots(self):
        return plt.figure(), self.ax

class MockAx:
    def bar(self, x, height):
        pass

    def set_title(self, title):
        pass

    def set_ylabel(self, label):
        pass

@pytest.fixture
def mock_plt(monkeypatch):
    mock_subplots = MockSubplots()
    monkeypatch.setattr(plt, 'subplots', mock_subplots.subplots)
    return mock_subplots

def test_task_func_empty_data():
    with pytest.raises(ValueError, match="Input data is empty."):
        task_func([])

def test_task_func_not_list_of_dicts():
    with pytest.raises(TypeError, match="Input must be a list of dictionaries."):
        task_func([1, 2, 3])

def test_task_func_non_numeric_values():
    with pytest.raises(TypeError, match="All values in the dictionaries must be numeric."):
        task_func([{"a": "not a number"}, {"b": 2}])

def test_task_func_valid_data(mock_plt):
    data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    expected_stats = {
        "a": {"mean": 2.0, "std": 1.4142135623730951},
        "b": {"mean": 3.0, "std": 1.4142135623730951}
    }
    stats, axes = task_func(data)
    assert stats == expected_stats
    assert len(axes) == 2
    assert isinstance(axes[0], MockAx)
    assert isinstance(axes[1], MockAx)

def test_task_func_single_dict(mock_plt):
    data = [{"a": 1}]
    expected_stats = {
        "a": {"mean": 1.0, "std": 0.0}
    }
    stats, axes = task_func(data)
    assert stats == expected_stats
    assert len(axes) == 1
    assert isinstance(axes[0], MockAx)