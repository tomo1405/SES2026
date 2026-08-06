import numpy as np
import pandas as pd
from src_0047 import task_func


def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
    # Fill missing values with column's average
    df = df.fillna(df.mean(axis=0))
    # Compute Z-scores
    df = df.apply(zscore)
    # Plot histograms for each numeric column
    axes = df.hist(grid=False, bins=10, layout=(1, df.shape[1]))
    plt.tight_layout()
    # Check that the output is a tuple with two elements
    assert isinstance(task_func(df), tuple)
    # Check that the first element is a dataframe
    assert isinstance(task_func(df)[0], pd.DataFrame)
    # Check that the second element is a list of axes
    assert isinstance(task_func(df)[1], list)
    # Check that the length of the list is equal to the number of numeric columns
    assert len(task_func(df)[1]) == df.select_dtypes(include=np.number).shape[1]
    # Check that the histograms are plotted correctly
    assert task_func(df)[1][0].get_xlabel() == 'A'
    assert task_func(df)[1][0].get_ylabel() == 'Frequency'
    assert task_func(df)[1][1].get_xlabel() == 'B'
    assert task_func(df)[1][1].get_ylabel() == 'Frequency'