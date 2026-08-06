import pytest
from src_0619 import task_func
import pandas as pd

@pytest.fixture
def mock_randint(monkeypatch):
    def mockrandint(a, b):
        return 3  # Fixed value for deterministic testing
    monkeypatch.setattr('random.randint', mockrandint)

def test_task_func(mock_randint):
    goals = 5
    penalties = 2
    results_df, plots = task_func(goals, penalties)

    # Check if the DataFrame has the correct shape
    assert isinstance(results_df, pd.DataFrame)
    assert results_df.shape == (5, 3)  # 5 teams, 3 columns

    # Check if the DataFrame columns are correct
    assert list(results_df.columns) == ['Team', 'Goals', 'Penalty Cost']

    # Check if the DataFrame values are as expected
    expected_teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    expected_goals = [3, 3, 3, 3, 3]  # Since randint is mocked to return 3
    expected_penalty_costs = [3000, 3000, 3000, 3000, 3000]  # 3 penalties * 1000 cost

    assert list(results_df['Team']) == expected_teams
    assert list(results_df['Goals']) == expected_goals
    assert list(results_df['Penalty Cost']) == expected_penalty_costs

    # Check if the plots are created correctly
    assert len(plots) == 2
    assert isinstance(plots[0], sns.axisgrid.BarPlotter)
    assert isinstance(plots[1], sns.axisgrid.BarPlotter)