import pytest
import pandas as pd
from src_1085 import task_func
import numpy as np

# Mocking the plt.show() function to prevent GUI display during tests
import matplotlib.pyplot as plt
plt.show = lambda: None

@pytest.fixture
def mock_data(tmpdir):
    data = {
        'A': ['1.0', '2.0', '3.0'],
        'B': ['4.0', '5.0', '6.0'],
        'C': ['7.0', '8.0', '9.0']
    }
    df = pd.DataFrame(data)
    file_path = tmpdir.join("data.csv")
    df.to_csv(file_path, index=False)
    return str(file_path)

def test_task_func(mock_data):
    means, std_devs, axes, anova_results = task_func(mock_data)
    
    # Check that means and std_devs are pandas Series
    assert isinstance(means, pd.Series)
    assert isinstance(std_devs, pd.Series)
    
    # Check that axes is a list of matplotlib Axes objects
    assert isinstance(axes, list)
    assert all(isinstance(ax, plt.Axes) for ax in axes)
    
    # Check that anova_results is a DataFrame when there are more than one column
    assert isinstance(anova_results, pd.DataFrame)
    
    # Check that the DataFrame has the correct shape and index
    assert anova_results.shape == (2, len(['A', 'B', 'C']))
    assert all(index in anova_results.index for index in ['F-value', 'P-value'])
    
    # Check that the DataFrame has the correct columns
    assert all(col in anova_results.columns for col in ['A', 'B', 'C'])

def test_task_func_single_column(mock_data):
    # Modify the mock data to have only one column
    df = pd.read_csv(mock_data)
    df.drop('B', axis=1, inplace=True)
    df.drop('C', axis=1, inplace=True)
    df.to_csv(mock_data, index=False)
    
    means, std_devs, axes, anova_results = task_func(mock_data)
    
    # Check that anova_results is None when there is only one column
    assert anova_results is None