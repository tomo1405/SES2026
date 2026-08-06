import pytest
from src_0523 import task_func
import collections
import matplotlib.pyplot as plt
import io
import sys

def test_task_func_empty_data():
    assert task_func([]) is None

def test_task_func_single_dict():
    data = [{'Alice': 85}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Average Student Scores"
    assert ax.get_xlabel() == "Student"
    assert ax.get_ylabel() == "Average Score"
    assert ax.patches[0].get_height() == 85

def test_task_func_multiple_dicts():
    data = [{'Alice': 85}, {'Bob': 90}, {'Alice': 70}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Average Student Scores"
    assert ax.get_xlabel() == "Student"
    assert ax.get_ylabel() == "Average Score"
    heights = [patch.get_height() for patch in ax.patches]
    assert heights == [77.5, 90]

def test_task_func_negative_score():
    data = [{'Alice': -10}]
    with pytest.raises(ValueError, match="Scores must be non-negative."):
        task_func(data)

def test_task_func_none_value():
    data = [{'Alice': None}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0

def test_task_func_order_of_keys():
    data = [{'Charlie': 80}, {'Alice': 90}, {'Bob': 70}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    labels = [label.get_text() for label in ax.get_xticklabels()]
    assert labels == ['Alice', 'Bob', 'Charlie']

def test_task_func_no_data_with_none_values():
    data = [{'Alice': None}, {'Bob': None}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0

def test_task_func_plot_color():
    data = [{'Alice': 85}, {'Bob': 90}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    colors = [patch.get_facecolor()[0] for patch in ax.patches]
    assert colors == [1.0, 0.0]  # Red and Yellow in RGBA format

# Redirect stdout to capture plot output
@pytest.fixture(autouse=True)
def capture_stdout():
    sys.stdout = io.StringIO()
    yield
    sys.stdout = sys.__stdout__