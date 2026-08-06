import pytest
from src_0263 import task_func
import collections
import seaborn as sns
import matplotlib.pyplot as plt
import io
import contextlib

@pytest.fixture
def sample_dict():
    return {'a': 1, 'b': 2, 'c': 3}

def test_task_func_adds_key_value_pair(sample_dict):
    new_key = 'd'
    new_value = 4
    updated_dict, _ = task_func(sample_dict, new_key, new_value)
    assert updated_dict == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def test_task_func_plots_distribution(sample_dict):
    new_key = 'd'
    new_value = 2  # To ensure the value already exists in the dictionary
    _, ax = task_func(sample_dict, new_key, new_value)
    assert isinstance(ax, sns.axisgrid.BarPlotter)

def test_task_func_plot_labels(sample_dict):
    new_key = 'd'
    new_value = 2
    _, ax = task_func(sample_dict, new_key, new_value)
    assert ax.get_title() == "Distribution of Dictionary Values"
    assert ax.get_xlabel() == "Values"
    assert ax.get_ylabel() == "Counts"

@contextlib.contextmanager
def no_display():
    """Suppress plotting output."""
    devnull = io.StringIO()
    with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
        yield

def test_task_func_no_display(sample_dict):
    new_key = 'd'
    new_value = 2
    with no_display():
        task_func(sample_dict, new_key, new_value)