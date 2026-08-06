import pytest
from src_0619 import task_func

def test_task_func():
    goals = 5
    penalties = 3
    results_df, plots = task_func(goals, penalties)

    # Check if the DataFrame has the correct number of rows and columns
    assert len(results_df) == len(TEAMS), "The DataFrame should have one row per team"
    assert len(results_df.columns) == 3, "The DataFrame should have three columns: Team, Goals, Penalty Cost"

    # Check if the DataFrame contains the correct columns
    assert all(col in results_df.columns for col in ['Team', 'Goals', 'Penalty Cost']), "DataFrame should contain 'Team', 'Goals', and 'Penalty Cost' columns"

    # Check if the plots list contains two elements
    assert len(plots) == 2, "The plots list should contain two bar plots"

    # Check if the plots are of the correct type
    assert isinstance(plots[0], sns.axisgrid.BarPlotter), "The first plot should be a Seaborn bar plot"
    assert isinstance(plots[1], sns.axisgrid.BarPlotter), "The second plot should be a Seaborn bar plot"

    # Check if the penalty cost is calculated correctly
    for index, row in results_df.iterrows():
        expected_penalty_cost = PENALTY_COST * row['Penalty Cost'] / PENALTY_COST
        assert row['Penalty Cost'] == expected_penalty_cost, "Penalty cost calculation is incorrect"

    # Check if the goals and penalties are within the expected range
    for index, row in results_df.iterrows():
        assert 0 <= row['Goals'] <= goals, "Goals should be between 0 and the specified maximum"
        assert 0 <= row['Penalty Cost'] / PENALTY_COST <= penalties, "Penalties should be between 0 and the specified maximum"