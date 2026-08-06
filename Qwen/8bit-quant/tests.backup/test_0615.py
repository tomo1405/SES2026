import pytest
from src_0615 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    goals = {
        'Team A': 10,
        'Team B': 8,
        'Team C': 12,
        'Team D': 7,
        'Team E': 9
    }
    penalties = {
        'Team A': 3,
        'Team B': 2,
        'Team C': 4,
        'Team D': 1,
        'Team E': 3
    }
    return goals, penalties

def test_task_func(sample_data):
    goals, penalties = sample_data
    df, plot = task_func(goals, penalties)

    # Check DataFrame
    expected_columns = ['Team', 'Goals', 'Penalties']
    assert list(df.columns) == expected_columns, "DataFrame columns do not match expected output"
    
    expected_teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert all(team in df['Team'].values for team in expected_teams), "DataFrame does not contain all expected teams"
    
    # Check PairPlot
    assert isinstance(plot, sns.axisgrid.PairGrid), "Return value is not a Seaborn PairGrid object"
    
    # Clean up plot to avoid interference with other tests
    plt.close('all')