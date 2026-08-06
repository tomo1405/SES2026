import pytest
from src_0344 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Mocking the plt.show to avoid actual plotting
plt.show = lambda: None

def test_task_func_basic():
    # Create a sample DataFrame
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A']}
    df = pd.DataFrame(data)
    
    # Call the function
    ax = task_func(df, 'Category')
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes)

def test_task_func_with_title():
    # Create a sample DataFrame
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A']}
    df = pd.DataFrame(data)
    
    # Call the function with a title
    ax = task_func(df, 'Category', title='Test Pie Chart')
    
    # Check if the title is set correctly
    assert ax.get_title() == 'Test Pie Chart'

def test_task_func_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Expect a ValueError to be raised
    with pytest.raises(ValueError):
        task_func(df, 'Category')

def test_task_func_nonexistent_column():
    # Create a sample DataFrame
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A']}
    df = pd.DataFrame(data)
    
    # Expect a ValueError to be raised for a non-existent column
    with pytest.raises(ValueError):
        task_func(df, 'NonExistentColumn')

def test_task_func_single_color():
    # Create a sample DataFrame with a single unique value
    data = {'Category': ['A', 'A', 'A', 'A', 'A', 'A']}
    df = pd.DataFrame(data)
    
    # Call the function
    ax = task_func(df, 'Category')
    
    # Check if only one color is used
    assert len(ax.patches) == 1
    assert ax.patches[0].get_facecolor() == (1.0, 0.0, 0.0, 1.0)  # Red color

def test_task_func_multiple_colors():
    # Create a sample DataFrame with multiple unique values
    data = {'Category': ['A', 'B', 'C', 'D', 'E', 'F']}
    df = pd.DataFrame(data)
    
    # Call the function
    ax = task_func(df, 'Category')
    
    # Check if the correct number of colors is used
    assert len(ax.patches) == 6
    for i, patch in enumerate(ax.patches):
        assert patch.get_facecolor() == (COLORS[i % len(COLORS)][0], COLORS[i % len(COLORS)][1], COLORS[i % len(COLORS)][2], 1.0)