import pytest
from src_0619 import task_func
import pandas as pd

def test_task_func():
    goals = 5
    penalties = 3
    results_df, plots = task_func(goals, penalties)

    # Check if the returned DataFrame has the correct shape
    assert isinstance(results_df, pd.DataFrame)
    assert results_df.shape == (5, 3)  # 5 teams, 3 columns (Team, Goals, Penalty Cost)

    # Check if the DataFrame contains the correct columns
    expected_columns = ['Team', 'Goals', 'Penalty Cost']
    assert list(results_df.columns) == expected_columns

    # Check if the Teams column contains the correct values
    assert all(team in results_df['Team'].values for team in ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'])

    # Check if the Goals and Penalty Cost are within the expected range
    assert all(0 <= goal <= goals for goal in results_df['Goals'])
    assert all(0 <= penalty_cost <= PENALTY_COST * penalties for penalty_cost in results_df['Penalty Cost'])

    # Check if the plots are returned correctly
    assert len(plots) == 2
    assert isinstance(plots[0], sns.axisgrid.BarPlotter)
    assert isinstance(plots[1], sns.axisgrid.BarPlotter)