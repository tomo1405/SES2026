import pytest
from src_0619 import task_func

@pytest.mark.parametrize("goals,penalties,expected_results", [
    (10, 5, 'Team A'),
    (20, 10, 'Team B'),
    (30, 15, 'Team C'),
    (40, 20, 'Team D'),
    (50, 25, 'Team E'),
])
def test_task_func(goals, penalties, expected_results):
    results_df, plots = task_func(goals, penalties)
    assert results_df['Team'].iloc[0] == expected_results

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(-10, 5)