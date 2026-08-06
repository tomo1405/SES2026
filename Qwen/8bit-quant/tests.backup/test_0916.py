import pytest
from src_0916 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        'closing_price': [100, 102, 101, 105, 110, 108, 107, 115, 113, 112]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    outliers, ax = task_func(sample_data)
    
    # Check if the outliers DataFrame is correctly identified
    expected_outliers = sample_data.iloc[[7, 8]]
    assert outliers.equals(expected_outliers), "The outliers DataFrame is not correct"
    
    # Check if the plot is created with the correct elements
    lines = ax.get_lines()
    assert len(lines) == 2, "There should be two lines in the plot (normal and outliers)"
    
    normal_line = lines[0]
    outlier_line = lines[1]
    
    assert normal_line.get_color() == 'blue', "The normal line should be blue"
    assert outlier_line.get_marker() == 'X', "The outlier points should be marked with 'X'"
    assert outlier_line.get_color() == 'red', "The outlier points should be red"
    assert outlier_line.get_markersize() == 12, "The outlier points should have a markersize of 12"
    
    # Check if the plot has the correct labels and title
    assert ax.get_xlabel() == 'Index', "The x-axis label should be 'Index'"
    assert ax.get_ylabel() == 'Closing Price', "The y-axis label should be 'Closing Price'"
    assert ax.get_title() == 'Outliers in Closing Prices', "The plot title should be 'Outliers in Closing Prices'"
    
    # Close the plot to avoid it showing during tests
    plt.close(fig)