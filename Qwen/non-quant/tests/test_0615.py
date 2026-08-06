import matplotlib.pyplot as plt
import pytest
import seaborn as sns
from src_0615 import task_func


@pytest.fixture
def sample_data():
    goals = {
        'Team A': 10,
        'Team B': 15,
        'Team C': 7,
        'Team D': 8,
        'Team E': 12
    }
    penalties = {
        'Team A': 3,
        'Team B': 5,
        'Team C': 2,
        'Team D': 4,
        'Team E': 6
    }
    return goals, penalties

def test_task_func_output(sample_data):
    goals, penalties = sample_data
    df, plot = task_func(goals, penalties)

    # Check DataFrame
    expected_columns = ['Team', 'Goals', 'Penalties']
    assert list(df.columns) == expected_columns
    assert len(df) == 5

    # Check DataFrame values
    for team in ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']:
        team_goals = goals.get(team, 0)
        team_penalties = penalties.get(team, 0)
        row = df[df['Team'] == team]
        assert row['Goals'].values[0] == team_goals
        assert row['Penalties'].values[0] == team_penalties

    # Check PairPlot
    assert isinstance(plot, sns.axisgrid.PairGrid)
    plt.close(plot.fig)  # Close the plot to prevent it from displaying during tests

def test_task_func_empty_input():
    goals = {}
    penalties = {}
    df, plot = task_func(goals, penalties)

    # Check DataFrame
    expected_columns = ['Team', 'Goals', 'Penalties']
    assert list(df.columns) == expected_columns
    assert len(df) == 0

    # Check PairPlot
    assert isinstance(plot, sns.axisgrid.PairGrid)
    plt.close(plot.fig)  # Close the plot to prevent it from displaying during tests

def test_task_func_partial_input(sample_data):
    goals, penalties = sample_data
    del goals['Team A']
    del penalties['Team B']
    df, plot = task_func(goals, penalties)

    # Check DataFrame
    expected_columns = ['Team', 'Goals', 'Penalties']
    assert list(df.columns) == expected_columns
    assert len(df) == 4

    # Check DataFrame values
    for team in ['Team C', 'Team D', 'Team E']:
        team_goals = goals.get(team, 0)
        team_penalties = penalties.get(team, 0)
        row = df[df['Team'] == team]
        assert row['Goals'].values[0] == team_goals
        assert row['Penalties'].values[0] == team_penalties

    # Check PairPlot
    assert isinstance(plot, sns.axisgrid.PairGrid)
    plt.close(plot.fig)  # Close the plot to prevent it from displaying during tests