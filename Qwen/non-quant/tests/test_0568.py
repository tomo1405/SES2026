import pytest
from src_0568 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Mocking the plt.show() function to prevent actual plotting
@pytest.fixture(autouse=True)
def mock_show(monkeypatch):
    def mock():
        pass
    monkeypatch.setattr(plt, 'show', mock)

def test_task_func():
    # Test with a simple input
    data = "1-2-3-4-5"
    result = task_func(data)
    
    # Check if the returned object is an Axes instance
    assert isinstance(result, plt.Axes)
    
    # Check if the DataFrame is created correctly
    expected_df = pd.DataFrame([1, 2, 3, 4, 5], columns=['Values'])
    assert result.get_lines()[0].get_data()[1][0] == expected_df['Values'].value_counts().iloc[0]
    
    # Check if the histogram is plotted correctly
    xticks = result.get_xticks()
    assert all(x in xticks for x in expected_df['Values'].unique())

# Test with different input
def test_task_func_with_different_input():
    data = "10-20-30-40-50"
    result = task_func(data)
    
    # Check if the returned object is an Axes instance
    assert isinstance(result, plt.Axes)
    
    # Check if the DataFrame is created correctly
    expected_df = pd.DataFrame([10, 20, 30, 40, 50], columns=['Values'])
    assert result.get_lines()[0].get_data()[1][0] == expected_df['Values'].value_counts().iloc[0]
    
    # Check if the histogram is plotted correctly
    xticks = result.get_xticks()
    assert all(x in xticks for x in expected_df['Values'].unique())