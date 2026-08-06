import pytest
from src_0619 import task_func

def test_task_func():
    goals = 10
    penalties = 5
    expected_results_df = ...  # Define the expected results DataFrame
    expected_plots = ...  # Define the expected plots

    results_df, plots = task_func(goals, penalties)

    assert results_df.equals(expected_results_df)
    assert plots == expected_plots