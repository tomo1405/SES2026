import pytest
from src_0520 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

# Mocking plt.show to prevent actual plotting
plt.ioff()

@pytest.fixture
def sample_data():
    return {
        'apple': [10, 20, 30],
        'banana': [15, 25, 35],
        'orange': [5, 15, 25]
    }

def test_task_func(sample_data):
    ax = task_func(sample_data)
    
    # Check if the axes object is created
    assert isinstance(ax, plt.Axes)
    
    # Check if the plot has the correct number of lines
    assert len(ax.lines) == len(sample_data)
    
    # Check if the labels and title are set correctly
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Sales Quantity"
    assert ax.get_title() == "Fruit Sales over Time"
    
    # Check if the legend contains the correct labels
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert set(legend_labels) == set(sample_data.keys())

# Restore plt.show after tests
plt.ion()