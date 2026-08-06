import pytest
from src_1024 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame for testing
@pytest.fixture
def sample_dataframe():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6]
    }
    return pd.DataFrame(data)

def test_task_func(sample_dataframe):
    result = task_func(sample_dataframe)
    assert result is not None

def test_empty_dataframe():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

def test_non_numeric_columns():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c']
    })
    with pytest.raises(TypeError):
        task_func(data)

def test_less_than_two_columns():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError):
        task_func(data)

def test_correlation_calculation(sample_dataframe):
    result = task_func(sample_dataframe)
    assert result is not None
    assert isinstance(result, plt.Axes)

def test_plot_visualization(sample_dataframe):
    result = task_func(sample_dataframe)
    assert result is not None
    assert isinstance(result, plt.Axes)