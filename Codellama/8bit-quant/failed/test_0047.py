import pytest
from src_0047 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    # Fill missing values with column's average
    df = df.fillna(df.mean(axis=0))
    # Compute Z-scores
    df = df.apply(zscore)
    # Plot histograms for each numeric column
    axes = df.hist(grid=False, bins=10, layout=(1, df.shape[1]))
    plt.tight_layout()
    # Check that the output is a tuple with two elements
    assert isinstance(task_func(df), tuple)
    # Check that the first element of the tuple is a dataframe
    assert isinstance(task_func(df)[0], pd.DataFrame)
    # Check that the second element of the tuple is a list of axes
    assert isinstance(task_func(df)[1], list)
    # Check that the length of the list of axes is equal to the number of numeric columns
    assert len(task_func(df)[1]) == df.shape[1]
    # Check that the histograms are plotted correctly
    assert np.all(task_func(df)[1][0].get_xlim() == (0, 1))
    assert np.all(task_func(df)[1][1].get_xlim() == (0, 1))
    assert np.all(task_func(df)[1][2].get_xlim() == (0, 1))
    # Check that the histograms are not overlapping
    assert np.all(task_func(df)[1][0].get_ylim() == (0, 1))
    assert np.all(task_func(df)[1][1].get_ylim() == (0, 1))
    assert np.all(task_func(df)[1][2].get_ylim() == (0, 1))
    # Check that the histograms are not overlapping
    assert np.all(task_func(df)[1][0].get_xlim() != task_func(df)[1][1].get_xlim())
    assert np.all(task_func(df)[1][0].get_xlim() != task_func(df)[1][2].get_xlim())
    assert np.all(task_func(df)[1][1].get_xlim() != task_func(df)[1][2].get_xlim())
    # Check that the histograms are not overlapping
    assert np.all(task_func(df)[1][0].get_ylim() != task_func(df)[1][1].get_ylim())
    assert np.all(task_func(df)[1][0].get_ylim() != task_func(df)[1][2].get_ylim())
    assert np.all(task_func(df)[1][1].get_ylim() != task_func(df)[1][2].get_ylim())