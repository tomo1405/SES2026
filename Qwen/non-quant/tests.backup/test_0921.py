import pytest
from src_0921 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Test with a simple dataset
    data = {
        'A': [1, 2, 3, 4],
        'B': [4, 3, 2, 1],
        'C': [2, 3, 4, 5]
    }
    ax = task_func(data)
    
    # Check if the returned object is a matplotlib Axes
    assert isinstance(ax, plt.Axes)
    
    # Check if the title is set correctly
    assert ax.get_title() == 'Correlation Matrix'
    
    # Check if the heatmap has annotations
    text = [text.get_text() for text in ax.texts]
    expected_annotations = ['1.00', '-1.00', '1.00', '-1.00', '1.00', '0.83']
    assert sorted(text) == sorted(expected_annotations)

# To run the tests, use the command: pytest -v