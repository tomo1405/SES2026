import pytest
from src_0037 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Input DataFrame contains only positive values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    transformed_df, fig = task_func(df)
    assert (transformed_df <= 0).any().any() == False
    assert transformed_df.equals(df)
    assert fig.axes[0].get_legend() == None

    # Test case 2: Input DataFrame contains negative values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    transformed_df, fig = task_func(df)
    assert (transformed_df <= 0).any().any() == True
    assert transformed_df.equals(df)
    assert fig.axes[0].get_legend() == None

    # Test case 3: Input DataFrame contains constant values
    df = pd.DataFrame({'A': [1, 1, 1], 'B': [1, 1, 1]})
    transformed_df, fig = task_func(df)
    assert (transformed_df <= 0).any().any() == False
    assert transformed_df.equals(df)
    assert fig.axes[0].get_legend() == None

    # Test case 4: Input DataFrame contains non-constant values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    transformed_df, fig = task_func(df)
    assert (transformed_df <= 0).any().any() == False
    assert transformed_df.equals(df)
    assert fig.axes[0].get_legend() == None

    # Test case 5: Input DataFrame contains null values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    transformed_df, fig = task_func(df)
    assert (transformed_df <= 0).any().any() == False
    assert transformed_df.equals(df)
    assert fig.axes[0].get_legend() == None

    # Test case 6: Input DataFrame contains non-numeric values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    transformed_df, fig = task_func(df)
    assert (transformed_df <= 0).any().any() == False
    assert transformed_df.equals(df)
    assert fig.axes[0].get_legend() == None

    # Test case 7: Input DataFrame contains non-numeric values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    transformed_df, fig = task_func(df)
    assert (transformed_df <= 0).any().any() == False
    assert transformed_df.equals(df)
    assert fig.axes[0].get_legend() == None

    # Test case 8: Input DataFrame contains non-numeric values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    transformed_df, fig = task_func(df)
    assert (transformed_df <= 0).any().any() == False
    assert transformed_df.equals(df)
    assert fig.axes[0].get_legend() == None

    # Test case 9: Input DataFrame contains non-numeric values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    transformed_df, fig = task_func(df)
    assert (transformed_df <= 0).any().any() == False
    assert transformed_df.equals(df)
    assert fig.axes[0].get_legend() == None

    # Test case 10: Input DataFrame contains non-numeric values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    transformed_df, fig = task_func(df)
    assert (transformed_df <= 0).any().any() == False
    assert transformed_df.equals(df)
    assert fig.axes[0].get_legend() == None