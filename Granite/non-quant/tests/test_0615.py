import pandas as pd
import seaborn as sns
import pytest

from src_0615 import task_func

def test_task_func():
    goals = {'Team A': 3, 'Team B': 2, 'Team C': 1, 'Team D': 5, 'Team E': 4}
    penalties = {'Team A': 1, 'Team B': 2, 'Team C': 3, 'Team D': 0, 'Team E': 4}
    expected_df = pd.DataFrame([
        ['Team A', 3, 1],
        ['Team B', 2, 2],
        ['Team C', 1, 3],
        ['Team D', 5, 0],
        ['Team E', 4, 4]
    ], columns=['Team', 'Goals', 'Penalties'])
    expected_plot = sns.pairplot(expected_df, hue='Team')

    df, plot = task_func(goals, penalties)

    assert df.equals(expected_df)
    assert plot == expected_plot