import pytest
from src_0063 import task_func
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Mocking the random.choice function to control the color selection
class MockRandom:
    def choice(self, seq):
        return 'b'  # Always return 'b' for consistent testing

@pytest.fixture(autouse=True)
def mock_random(monkeypatch):
    monkeypatch.setattr(random, 'random', MockRandom())

def test_task_func_with_valid_data():
    result = [{'from_user': 10}, {'from_user': 20}, {'from_user': 30}]
    with plt.FigureCanvas(plt.figure()) as canvas:
        task_func(result)
        assert len(canvas.get_axes()) == 1
        ax = canvas.get_axes()[0]
        assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_with_missing_key():
    result = [{'not_from_user': 10}, {'not_from_user': 20}, {'not_from_user': 30}]
    with plt.FigureCanvas(plt.figure()) as canvas:
        task_func(result)
        assert len(canvas.get_axes()) == 1
        ax = canvas.get_axes()[0]
        assert ax.get_lines() == []  # No data should be plotted

def test_task_func_with_empty_list():
    result = []
    with plt.FigureCanvas(plt.figure()) as canvas:
        task_func(result)
        assert len(canvas.get_axes()) == 1
        ax = canvas.get_axes()[0]
        assert ax.get_lines() == []  # No data should be plotted

def test_task_func_with_no_from_user_values():
    result = [{'from_user': None}, {'from_user': None}, {'from_user': None}]
    with plt.FigureCanvas(plt.figure()) as canvas:
        task_func(result)
        assert len(canvas.get_axes()) == 1
        ax = canvas.get_axes()[0]
        assert ax.get_lines() == []  # No data should be plotted