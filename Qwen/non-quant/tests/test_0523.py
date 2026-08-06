import pytest
from src_0523 import task_func
import matplotlib.pyplot as plt
import io
import sys

# Mocking the plt.subplots to capture the figure
class MockFigure:
    def bar(self, labels, values, color):
        pass

    def set_title(self, title):
        pass

    def set_xlabel(self, label):
        pass

    def set_ylabel(self, label):
        pass

class MockAxes:
    def __init__(self):
        self.figure = MockFigure()

@pytest.fixture
def mock_plt(mocker):
    mocker.patch('matplotlib.pyplot.subplots', return_value=(MockFigure(), MockAxes()))

def test_task_func_empty_data(mock_plt):
    result = task_func([])
    assert result is None

def test_task_func_single_dict(mock_plt):
    data = [{'Alice': 85}]
    result = task_func(data)
    assert isinstance(result, MockAxes)

def test_task_func_multiple_dicts(mock_plt):
    data = [{'Alice': 85}, {'Bob': 90}, {'Alice': 78}]
    result = task_func(data)
    assert isinstance(result, MockAxes)

def test_task_func_negative_score(mock_plt):
    data = [{'Alice': -85}]
    with pytest.raises(ValueError, match="Scores must be non-negative."):
        task_func(data)

def test_task_func_none_score(mock_plt):
    data = [{'Alice': None}]
    result = task_func(data)
    assert result is None

def test_task_func_with_duplicates(mock_plt):
    data = [{'Alice': 85}, {'Alice': 90}, {'Bob': 88}]
    result = task_func(data)
    assert isinstance(result, MockAxes)