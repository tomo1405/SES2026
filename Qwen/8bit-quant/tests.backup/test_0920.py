import pytest
from src_0920 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

# Mocking plt.show to avoid opening a window
plt.ioff()

@pytest.fixture
def sample_data():
    return [
        {'category': 'A'},
        {'category': 'B'},
        {'category': 'A'},
        {'category': 'C'},
        {'category': 'E'},
        {'category': 'B'},
        {'category': 'D'},
        {'category': 'A'},
        {'category': 'C'},
        {'category': 'D'}
    ]

def test_task_func_with_sample_data(sample_data):
    ax = task_func(sample_data, 'category')
    assert isinstance(ax, plt.Axes)
    expected_categories = ['A', 'B', 'C', 'D', 'E']
    assert list(ax.get_xticklabels()) == expected_categories
    # Check if the counts are correct
    expected_counts = [4, 3, 2, 2, 1]
    actual_counts = [bar.get_height() for bar in ax.patches]
    assert actual_counts == expected_counts

def test_task_func_with_missing_categories(sample_data):
    # Remove some categories from the data
    modified_data = [d for d in sample_data if d['category'] not in ['B', 'D']]
    ax = task_func(modified_data, 'category')
    assert isinstance(ax, plt.Axes)
    expected_categories = ['A', 'B', 'C', 'D', 'E']
    assert list(ax.get_xticklabels()) == expected_categories
    # Check if the counts are correct, including zeros for missing categories
    expected_counts = [4, 0, 2, 0, 1]
    actual_counts = [bar.get_height() for bar in ax.patches]
    assert actual_counts == expected_counts

def test_task_func_with_empty_data():
    empty_data = []
    ax = task_func(empty_data, 'category')
    assert isinstance(ax, plt.Axes)
    expected_categories = ['A', 'B', 'C', 'D', 'E']
    assert list(ax.get_xticklabels()) == expected_categories
    # Check if all counts are zero
    expected_counts = [0, 0, 0, 0, 0]
    actual_counts = [bar.get_height() for bar in ax.patches]
    assert actual_counts == expected_counts

def test_task_func_with_invalid_column(sample_data):
    with pytest.raises(KeyError):
        task_func(sample_data, 'invalid_column')

def test_task_func_with_nonexistent_category(sample_data):
    # Add a category not in CATEGORIES
    sample_data.append({'category': 'F'})
    ax = task_func(sample_data, 'category')
    assert isinstance(ax, plt.Axes)
    expected_categories = ['A', 'B', 'C', 'D', 'E']
    assert list(ax.get_xticklabels()) == expected_categories
    # Check if the counts are correct, ignoring the invalid category
    expected_counts = [4, 3, 2, 2, 1]
    actual_counts = [bar.get_height() for bar in ax.patches]
    assert actual_counts == expected_counts