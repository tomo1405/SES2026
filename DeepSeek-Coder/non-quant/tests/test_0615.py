import pytest
from src_0615 import task_func

def test_task_func():
    goals = {
        'Team A': 10,
        'Team B': 5,
        'Team C': 7,
        'Team D': 3,
        'Team E': 8
    }
    penalties = {
        'Team A': 2,
        'Team B': 1,
        'Team C': 3,
        'Team D': 0,
        'Team E': 4
    }

    df, plot = task_func(goals, penalties)

    assert isinstance(df, pd.DataFrame), "The result should be a DataFrame"
    assert len(df) == 5, "The DataFrame should contain 5 rows"
    assert set(df['Team'].values) == {'Team A', 'Team B', 'Team C', 'Team D', 'Team E'}, "The DataFrame should contain the correct teams"
    assert df.loc[df['Team'] == 'Team A', 'Goals'].values[0] == 10, "The DataFrame should contain the correct goals for Team A"
    assert df.loc[df['Team'] == 'Team B', 'Goals'].values[0] == 5, "The DataFrame should contain the correct goals for Team B"
    assert df.loc[df['Team'] == 'Team C', 'Penalties'].values[0] == 3, "The DataFrame should contain the correct penalties for Team C"
    assert df.loc[df['Team'] == 'Team D', 'Penalties'].values[0] == 0, "The DataFrame should contain the correct penalties for Team D"
    assert df.loc[df['Team'] == 'Team E', 'Goals'].values[0] == 8, "The DataFrame should contain the correct goals for Team E"