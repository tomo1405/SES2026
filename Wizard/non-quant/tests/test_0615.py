python
import pandas as pd
import seaborn as sns
import pytest

def task_func(goals, penalties):
    # Constants
    TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']

    data = []
    for team in TEAMS:
        team_goals = goals.get(team, 0)
        team_penalties = penalties.get(team, 0)
        data.append([team, team_goals, team_penalties])

    df = pd.DataFrame(data, columns=['Team', 'Goals', 'Penalties'])

    plot = sns.pairplot(df, hue='Team')

    return df, plot

def test_task_func():
    # Test case 1
    goals = {'Team A': 5, 'Team B': 3, 'Team C': 2, 'Team D': 1, 'Team E': 0}
    penalties = {'Team A': 0, 'Team B': 1, 'Team C': 2, 'Team D': 3, 'Team E': 4}
    expected_df = pd.DataFrame({'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                                'Goals': [5, 3, 2, 1, 0],
                                'Penalties': [0, 1, 2, 3, 4]})
    expected_plot = None
    df, plot = task_func(goals, penalties)
    assert df.equals(expected_df)
    assert plot == expected_plot

    # Test case 2
    goals = {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}
    penalties = {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}
    expected_df = pd.DataFrame({'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                                'Goals': [0, 0, 0, 0, 0],
                                'Penalties': [0, 0, 0, 0, 0]})
    expected_plot = None
    df, plot = task_func(goals, penalties)
    assert df.equals(expected_df)
    assert plot == expected_plot

    # Test case 3
    goals = {'Team A': 1, 'Team B': 2, 'Team C': 3, 'Team D': 4, 'Team E': 5}
    penalties = {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}
    expected_df = pd.DataFrame({'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                                'Goals': [1, 2, 3, 4, 5],
                                'Penalties': [0, 0, 0, 0, 0]})
    expected_plot = None
    df, plot = task_func(goals, penalties)
    assert df.equals(expected_df)
    assert plot == expected_plot

    # Test case 4
    goals = {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}
    penalties = {'Team A': 1, 'Team B': 2, 'Team C': 3, 'Team D': 4, 'Team E': 5}
    expected_df = pd.DataFrame({'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                                'Goals': [0, 0, 0, 0, 0],
                                'Penalties': [1, 2, 3, 4, 5]})
    expected_plot = None
    df, plot = task_func(goals, penalties)
    assert df.equals(expected_df)
    assert plot == expected_plot

    # Test case 5
    goals = {'Team A': 1, 'Team B': 2, 'Team C': 3, 'Team D': 4, 'Team E': 5}
    penalties = {'Team A': 1, 'Team B': 2, 'Team C': 3, 'Team D': 4, 'Team E': 5}
    expected_df = pd.DataFrame({'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                                'Goals': [1, 2, 3, 4, 5],
                                'Penalties': [1, 2, 3, 4, 5]})
    expected_plot = None
    df, plot = task_func(goals, penalties)
    assert df.equals(expected_df)
    assert plot == expected_plot