python
import pytest
from src_0617 import task_func

def test_task_func():
    # Test with default parameters
    results_df, ax = task_func(5, 2)
    assert len(results_df) == 5
    assert len(results_df.columns) == 3
    assert results_df.columns.tolist() == ['Team', 'Goals', 'Penalty Cost']
    assert results_df['Goals'].sum() == 5
    assert results_df['Penalty Cost'].sum() == 2000
    assert ax.get_xlabel() == 'Team'
    assert ax.get_ylabel() == 'Results'
    assert ax.get_xticks() == [0, 1, 2, 3, 4]
    assert ax.get_xticklabels() == ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert ax.get_ylim() == (0, 5)
    assert ax.get_yticks() == [0, 1, 2, 3, 4, 5]
    assert ax.get_yticklabels() == ['0', '1', '2', '3', '4', '5']

    # Test with custom parameters
    results_df, ax = task_func(10, 5, teams=['Team 1', 'Team 2', 'Team 3'], penalty_cost=5000, rng_seed=42)
    assert len(results_df) == 3
    assert len(results_df.columns) == 3
    assert results_df.columns.tolist() == ['Team', 'Goals', 'Penalty Cost']
    assert results_df['Goals'].sum() == 10
    assert results_df['Penalty Cost'].sum() == 25000
    assert ax.get_xlabel() == 'Team'
    assert ax.get_ylabel() == 'Results'
    assert ax.get_xticks() == [0, 1, 2]
    assert ax.get_xticklabels() == ['Team 1', 'Team 2', 'Team 3']
    assert ax.get_ylim() == (0, 10)
    assert ax.get_yticks() == [0, 2, 4, 6, 8, 10]
    assert ax.get_yticklabels() == ['0', '2', '4', '6', '8', '10']