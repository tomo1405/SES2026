import pytest
from src_0613 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Sample input data
    goals = {
        'Team A': 10,
        'Team B': 5,
        'Team C': 8,
        'Team D': 3,
        'Team E': 7
    }
    penalties = {
        'Team A': 2,
        'Team B': 1,
        'Team C': 3,
        'Team D': 0,
        'Team E': 4
    }

    # Call the function with sample data
    result_df = task_func(goals, penalties)

    # Check if the DataFrame has the correct number of rows
    assert len(result_df) == 5, "The DataFrame should have 5 rows, one for each team."

    # Check if the DataFrame has the correct columns
    expected_columns = ['Team', 'Goals', 'Penalties', 'Penalties Cost', 'Performance Score']
    assert all(col in result_df.columns for col in expected_columns), "The DataFrame is missing one or more required columns."

    # Check if the 'Team' column contains the correct team names
    assert all(team in result_df['Team'].values for team in goals.keys()), "The 'Team' column should contain all team names from the input data."

    # Check if the 'Goals' and 'Penalties' columns have the correct values
    for team, team_goals in goals.items():
        team_row = result_df[result_df['Team'] == team]
        assert team_row['Goals'].values[0] == team_goals, f"The 'Goals' value for {team} is incorrect."

    for team, team_penalties in penalties.items():
        team_row = result_df[result_df['Team'] == team]
        assert team_row['Penalties'].values[0] == team_penalties, f"The 'Penalties' value for {team} is incorrect."

    # Check if the 'Penalties Cost' is within the expected range
    penalties_costs = [100, 200, 300, 400, 500]
    for index, row in result_df.iterrows():
        assert row['Penalties Cost'] in penalties_costs * row['Penalties'], f"The 'Penalties Cost' for {row['Team']} is incorrect."

    # Check if the 'Performance Score' is calculated correctly
    for team, team_goals in goals.items():
        team_penalties = penalties.get(team, 0)
        performance_score = max(0, team_goals - team_penalties)
        team_row = result_df[result_df['Team'] == team]
        assert team_row['Performance Score'].values[0] == performance_score, f"The 'Performance Score' for {team} is incorrect."

if __name__ == "__main__":
    pytest.main()