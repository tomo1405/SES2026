python
import pytest
import pandas as pd
import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Fill missing values with column's average
    df = df.fillna(df.mean(axis=0))
    # Compute Z-scores
    df = df.apply(zscore)
    # Plot histograms for each numeric column
    axes = df.hist(grid=False, bins=10, layout=(1, df.shape[1]))
    plt.tight_layout()
    return df, axes

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, np.nan], 'C': ['a', 'b', 'c']})
    expected_df = pd.DataFrame({'A': [-1.22474487, 0., 1.22474487],
                                'B': [-1.22474487, 0., 1.22474487],
                                'C': ['a', 'b', 'c']})
    expected_axes = [plt.Axes(plt.figure(), 0.1, 0.1, 0.8, 0.8)]
    expected_axes[0].set_title('A')
    expected_axes[0].set_xlabel('Z-score')
    expected_axes[0].set_ylabel('Frequency')
    expected_axes[0].set_xlim(-3, 3)
    expected_axes[0].set_ylim(0, 3)
    expected_axes[0].grid(False)
    expected_axes[0].hist(expected_df['A'], bins=10, range=(-3, 3), density=True)
    expected_axes[0].hist(expected_df['B'], bins=10, range=(-3, 3), density=True)
    actual_df, actual_axes = task_func(df)
    assert actual_df.equals(expected_df)
    assert len(actual_axes) == len(expected_axes)
    for i in range(len(actual_axes)):
        assert actual_axes[i].get_title() == expected_axes[i].get_title()
        assert actual_axes[i].get_xlabel() == expected_axes[i].get_xlabel()
        assert actual_axes[i].get_ylabel() == expected_axes[i].get_ylabel()
        assert actual_axes[i].get_xlim() == expected_axes[i].get_xlim()
        assert actual_axes[i].get_ylim() == expected_axes[i].get_ylim()
        assert actual_axes[i].get_gridlines() == expected_axes[i].get_gridlines()
        assert np.array_equal(actual_axes[i].get_lines()[0].get_data(), expected_axes[i].get_lines()[0].get_data())
        assert np.array_equal(actual_axes[i].get_lines()[1].get_data(), expected_axes[i].get_lines()[1].get_data())

    # Test case 2: Test with invalid input (empty dataframe)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test case 3: Test with invalid input (non-numeric column)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({'A': [1, 2, 3], 'B': ['4', '5', '6'], 'C': ['a', 'b', 'c']}))

    # Test case 4: Test with invalid input (non-numeric dataframe)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({'A': [1, 2, 3], 'B': ['4', '5', '6'], 'C': ['a', 'b', 'c']}))