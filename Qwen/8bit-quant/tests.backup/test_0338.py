import pytest
from src_0338 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'value': [10, 12, 15, 17, 20, 22]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    ax = task_func(sample_df, 'group', 'value')
    
    # Check if the returned object is a matplotlib Axes
    assert isinstance(ax, plt.Axes)
    
    # Check if the correct number of bars are plotted
    containers = ax.containers
    assert len(containers) == 1
    bars = containers[0]
    assert len(bars) == 3  # There should be 3 bars for 3 groups
    
    # Check if the x-ticks are set correctly
    xticklabels = [label.get_text() for label in ax.get_xticklabels()]
    assert xticklabels == ['A', 'B', 'C']
    
    # Check if the y-label is set correctly
    assert ax.get_ylabel() == 'value'
    
    # Check if the title is set correctly
    assert ax.get_title() == 'Bar chart of value by group'
    
    # Check if the legend is present
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == ['Group 1', 'Group 2', 'Group 3']
    
    # Clean up the plot
    plt.close(ax.figure)