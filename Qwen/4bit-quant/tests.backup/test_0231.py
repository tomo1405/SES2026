import pytest
from src_0231 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_invalid_input():
    # Test with None
    assert task_func(None) == "Invalid input"
    
    # Test with a list instead of DataFrame
    assert task_func([1, 2, 3]) == "Invalid input"
    
    # Test with a dictionary instead of DataFrame
    assert task_func({'key': 'value'}) == "Invalid input"

def test_task_func_valid_input():
    # Create a sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'Country': ['USA', 'Canada', 'USA', 'Canada'],
        'Score': [85, 90, 78, 85]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    result = task_func(df)
    
    # Check if the result is a matplotlib figure
    assert isinstance(result, plt.Figure)

def test_task_func_drop_duplicates():
    # Create a sample DataFrame with duplicates
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'Country': ['USA', 'Canada', 'USA', 'Canada'],
        'Score': [85, 90, 78, 85]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    result = task_func(df)
    
    # Check if duplicates are dropped
    assert len(result.axes[0]) == 3  # Only 3 unique names after dropping duplicates

def test_task_func_plots():
    # Create a sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Country': ['USA', 'Canada', 'USA'],
        'Score': [85, 90, 78]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    result = task_func(df)
    
    # Check if the figure has two subplots
    assert len(result.axes) == 2