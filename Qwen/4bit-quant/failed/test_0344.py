import pytest
from src_0344 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import io

# Mocking plt.show to prevent actual plotting
plt.ioff()

def test_task_func_with_valid_data():
    # Create a sample DataFrame
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A']}
    df = pd.DataFrame(data)
    
    # Call the function
    ax = task_func(df, 'Category', 'Category Distribution')
    
    # Check if the plot is created
    assert isinstance(ax, plt.AxesSubplot)
    
    # Check if the title is set correctly
    assert ax.get_title() == 'Category Distribution'

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Test that it raises a ValueError
    with pytest.raises(ValueError):
        task_func(df, 'Category')

def test_task_func_with_nonexistent_column():
    # Create a sample DataFrame
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A']}
    df = pd.DataFrame(data)
    
    # Test that it raises a ValueError
    with pytest.raises(ValueError):
        task_func(df, 'NonExistentColumn')

def test_task_func_with_less_colors_than_categories():
    # Create a sample DataFrame with more categories than colors
    data = {'Category': ['A', 'B', 'C', 'D', 'E']}
    df = pd.DataFrame(data)
    
    # Call the function
    ax = task_func(df, 'Category', 'Category Distribution')
    
    # Check if the plot is created
    assert isinstance(ax, plt.AxesSubplot)
    
    # Check if the number of patches matches the number of unique values
    assert len(ax.patches) == len(df['Category'].unique())

def test_task_func_without_title():
    # Create a sample DataFrame
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A']}
    df = pd.DataFrame(data)
    
    # Call the function without a title
    ax = task_func(df, 'Category')
    
    # Check if the plot is created
    assert isinstance(ax, plt.AxesSubplot)
    
    # Check if the title is not set
    assert ax.get_title() == ''

def test_task_func_with_more_colors_than_categories():
    # Create a sample DataFrame with fewer categories than colors
    data = {'Category': ['A', 'B', 'A', 'C']}
    df = pd.DataFrame(data)
    
    # Call the function
    ax = task_func(df, 'Category', 'Category Distribution')
    
    # Check if the plot is created
    assert isinstance(ax, plt.AxesSubplot)
    
    # Check if the number of patches matches the number of unique values
    assert len(ax.patches) == len(df['Category'].unique())