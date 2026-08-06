python
import pytest
from src_0618 import task_func

def test_task_func():
    # Test case 1: Test with default parameters
    results_df = task_func(5, 3)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.columns.tolist() == ['Team', 'Match Result']
    assert all(isinstance(result, str) for result in results_df['Match Result'])
    assert all(isinstance(goal, int) for goal in results_df['Goals'])
    assert all(isinstance(penalty, int) for penalty in results_df['Penalty Cost'])
    assert all(penalty <= PENALTY_COST for penalty in results_df['Penalty Cost'])
    assert all(goal <= 5 for goal in results_df['Goals'])
    assert all(penalty <= 3 for penalty in results_df['Penalty Cost'])

    # Test case 2: Test with custom parameters
    results_df = task_func(10, 5, rng_seed=42)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.columns.tolist() == ['Team', 'Match Result']
    assert all(isinstance(result, str) for result in results_df['Match Result'])
    assert all(isinstance(goal, int) for goal in results_df['Goals'])
    assert all(isinstance(penalty, int) for penalty in results_df['Penalty Cost'])
    assert all(penalty <= PENALTY_COST for penalty in results_df['Penalty Cost'])
    assert all(goal <= 10 for goal in results_df['Goals'])
    assert all(penalty <= 5 for penalty in results_df['Penalty Cost'])

    # Test case 3: Test with custom teams
    teams = ['Team 1', 'Team 2', 'Team 3']
    results_df = task_func(7, 4, teams=teams)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 3
    assert results_df.columns.tolist() == ['Team', 'Match Result']
    assert all(isinstance(result, str) for result in results_df['Match Result'])
    assert all(isinstance(goal, int) for goal in results_df['Goals'])
    assert all(isinstance(penalty, int) for penalty in results_df['Penalty Cost'])
    assert all(penalty <= PENALTY_COST for penalty in results_df['Penalty Cost'])
    assert all(goal <= 7 for goal in results_df['Goals'])
    assert all(penalty <= 4 for penalty in results_df['Penalty Cost'])

    # Test case 4: Test with empty dataframe
    results_df = task_func(0, 0)
    assert isinstance(results_df, pd.DataFrame)
    assert results_df.empty

    # Test case 5: Test with invalid goals and penalties
    with pytest.raises(ValueError):
        task_func(-1, 0)
    with pytest.raises(ValueError):
        task_func(0, -1)
    with pytest.raises(ValueError):
        task_func(-1, -1)