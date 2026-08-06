import pytest
from src_0613 import task_func

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]

# Test cases
goals = {'Team A': 3, 'Team B': 2, 'Team C': 1, 'Team D': 0, 'Team E': 0}
penalties = {'Team A': 2, 'Team B': 1, 'Team C': 0, 'Team D': 3, 'Team E': 0}
expected_report_data = [
    {'Team': 'Team A', 'Goals': 3, 'Penalties': 2, 'Penalties Cost': 200, 'Performance Score': 1},
    {'Team': 'Team B', 'Goals': 2, 'Penalties': 1, 'Penalties Cost': 100, 'Performance Score': 1},
    {'Team': 'Team C', 'Goals': 1, 'Penalties': 0, 'Penalties Cost': 0, 'Performance Score': 1},
    {'Team': 'Team D', 'Goals': 0, 'Penalties': 3, 'Penalties Cost': 1500, 'Performance Score': 0},
    {'Team': 'Team E', 'Goals': 0, 'Penalties': 0, 'Penalties Cost': 0, 'Performance Score': 0}
]
expected_report_df = pd.DataFrame(expected_report_data)

# Test the function with the given test cases
def test_task_func():
    report_df = task_func(goals, penalties)
    assert report_df.equals(expected_report_df)

# Run the test
test_task_func()