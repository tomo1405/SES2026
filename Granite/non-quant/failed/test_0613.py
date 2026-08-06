import pytest
from src_0613 import task_func

def test_task_func():
    goals = {'Team A': 3, 'Team B': 2, 'Team C': 1, 'Team D': 0, 'Team E': 4}
    penalties = {'Team A': 1, 'Team B': 2, 'Team C': 3, 'Team D': 0, 'Team E': 1}
    expected_report_data = [
        {'Team': 'Team A', 'Goals': 3, 'Penalties': 1, 'Penalties Cost': 100, 'Performance Score': 2},
        {'Team': 'Team B', 'Goals': 2, 'Penalties': 2, 'Penalties Cost': 200, 'Performance Score': 0},
        {'Team': 'Team C', 'Goals': 1, 'Penalties': 3, 'Penalties Cost': 300, 'Performance Score': -2},
        {'Team': 'Team D', 'Goals': 0, 'Penalties': 0, 'Penalties Cost': 0, 'Performance Score': 0},
        {'Team': 'Team E', 'Goals': 4, 'Penalties': 1, 'Penalties Cost': 500, 'Performance Score': 3}
    ]
    expected_report_df = pd.DataFrame(expected_report_data)

    report_df = task_func(goals, penalties)

    assert report_df.equals(expected_report_df)