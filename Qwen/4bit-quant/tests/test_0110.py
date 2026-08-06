import pytest
from src_0110 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

# Mocking plt.show to prevent GUI display during tests
plt.ioff()

def test_task_func_with_default_parameters():
    # Create a sample DataFrame
    data = {
        'Item': ['apple', 'banana', 'apple', 'grape', 'banana'],
        'Location': ['store1', 'store1', 'store2', 'store2', 'store3']
    }
    df = pd.DataFrame(data)

    # Call the function
    ax = task_func(df)

    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Item Distribution by Location'
    assert ax.get_ylabel() == 'Count'

def test_task_func_with_custom_items_and_locations():
    # Create a sample DataFrame
    data = {
        'Item': ['apple', 'banana', 'apple', 'grape', 'banana'],
        'Location': ['store1', 'store1', 'store2', 'store2', 'store3']
    }
    df = pd.DataFrame(data)

    # Define custom items and locations
    items = ['apple', 'banana', 'grape']
    locations = ['store1', 'store2']

    # Call the function
    ax = task_func(df, items=items, locations=locations)

    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Item Distribution by Location'
    assert ax.get_ylabel() == 'Count'

def test_task_func_invalid_df():
    # Create an invalid DataFrame
    data = {
        'Product': ['apple', 'banana', 'apple', 'grape', 'banana'],
        'Store': ['store1', 'store1', 'store2', 'store2', 'store3']
    }
    df = pd.DataFrame(data)

    # Check if ValueError is raised
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns."):
        task_func(df)

def test_task_func_empty_df():
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['Item', 'Location'])

    # Check if ValueError is raised
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns."):
        task_func(df)