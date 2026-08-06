import pytest
from src_1012 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

@pytest.fixture
def sample_csv_data():
    data = StringIO("column1,column2\nA,1\nA,2\nB,3\nB,4")
    return data

def test_task_func(sample_csv_data):
    ax = task_func(sample_csv_data, "column1", "column2")
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes)
    
    # Check if the plot has the correct title
    assert ax.get_title() == "Mean of column2 Grouped by column1"
    
    # Check if the plot has the correct x and y labels
    assert ax.get_xlabel() == "column1"
    assert ax.get_ylabel() == "Mean of column2"
    
    # Check if the bar heights are correct
    bars = ax.patches
    expected_heights = [1.5, 3.5]  # Mean of values for 'A' and 'B'
    actual_heights = [bar.get_height() for bar in bars]
    assert actual_heights == expected_heights
    
    # Check if the bar labels are correct
    expected_labels = ['A', 'B']
    actual_labels = [bar.get_x() + bar.get_width() / 2 for bar in bars]
    assert [ax.get_xticks()[int(round(label))] for label in actual_labels] == expected_labels