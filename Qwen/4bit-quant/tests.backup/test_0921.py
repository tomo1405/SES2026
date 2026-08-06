import pytest
from src_0921 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Create a sample dataset
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6]
    }
    
    # Call the function with the sample data
    ax = task_func(data)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib AxesSubplot object"
    
    # Check if the title of the plot is correct
    assert ax.get_title() == 'Correlation Matrix', "The plot title should be 'Correlation Matrix'"
    
    # Check if the heatmap is created correctly by verifying the number of annotations
    # This assumes that each cell in the heatmap has an annotation
    expected_annotations = len(data) ** 2  # Assuming a square matrix
    actual_annotations = len([text for text in ax.texts if isinstance(text, matplotlib.text.Text)])
    assert actual_annotations == expected_annotations, f"Expected {expected_annotations} annotations but got {actual_annotations}"

# Note: This test assumes that the seaborn and matplotlib libraries are installed and properly configured.