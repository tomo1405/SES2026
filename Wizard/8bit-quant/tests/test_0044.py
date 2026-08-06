python
import numpy as np
import pandas as pd
import seaborn as sns
import pytest

from src_0044 import task_func

def test_task_func():
    # Test case 1: Test with a dataframe with missing values
    df = pd.DataFrame({'A': [1, 2, 3, np.nan], 'B': [4, 5, np.nan, 7], 'C': [8, np.nan, 10, 11]})
    expected_description = pd.DataFrame({'count': [3.0, 2.0, 2.0, 2.0], 'mean': [2.0, 5.0, 8.0, 10.0], 'std': [1.0, 1.0, 1.0, 1.0], 'min': [1.0, 4.0, 8.0, 10.0], '25%': [1.0, 4.0, 8.0, 10.0], '50%': [2.0, 5.0, 8.0, 10.0], '75%': [3.0, 5.0, 8.0, 10.0], 'max': [3.0, 7.0, 10.0, 11.0]})
    expected_plots = [sns.displot(df['A'], bins=10).ax, sns.displot(df['B'], bins=10).ax, sns.displot(df['C'], bins=10).ax]
    description, plots = task_func(df)
    assert description.equals(expected_description)
    assert len(plots) == len(expected_plots)
    for i in range(len(plots)):
        assert plots[i].get_title() == expected_plots[i].get_title()

    # Test case 2: Test with a dataframe without missing values
    df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12]})
    expected_description = pd.DataFrame({'count': [4.0, 4.0, 4.0, 4.0], 'mean': [2.5, 6.5, 10.5, 14.5], 'std': [1.5811388300841898, 1.5811388300841898, 1.5811388300841898, 1.5811388300841898], 'min': [1.0, 5.0, 9.0, 13.0], '25%': [1.75, 5.75, 9.75, 13.75], '50%': [2.5, 6.5, 10.5, 14.5], '75%': [3.25, 7.25, 11.25, 15.25], 'max': [4.0, 8.0, 12.0, 16.0]})
    expected_plots = [sns.displot(df['A'], bins=10).ax, sns.displot(df['B'], bins=10).ax, sns.displot(df['C'], bins=10).ax]
    description, plots = task_func(df)
    assert description.equals(expected_description)
    assert len(plots) == len(expected_plots)
    for i in range(len(plots)):
        assert plots[i].get_title() == expected_plots[i].get_title()