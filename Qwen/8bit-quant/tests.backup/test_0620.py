import pytest
from src_0620 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func_output():
    # Test with fixed seed to ensure reproducibility
    rng_seed = 42
    goals = 5
    penalties = 3

    # Expected output structure
    expected_columns = ['Team', 'Goals', 'Penalty Cost']

    # Call the function
    results_df, model = task_func(goals, penalties, rng_seed)

    # Check if the DataFrame has the correct columns
    assert list(results_df.columns) == expected_columns

    # Check if the DataFrame has the correct number of rows
    assert len(results_df) == len(TEAMS)

    # Check if the model is an instance of LinearRegression
    assert isinstance(model, LinearRegression)

def test_task_func_randomness():
    # Test with different seeds to check randomness
    rng_seed1 = 42
    rng_seed2 = 99

    goals = 5
    penalties = 3

    # Call the function with two different seeds
    results_df1, _ = task_func(goals, penalties, rng_seed1)
    results_df2, _ = task_func(goals, penalties, rng_seed2)

    # Check if the DataFrames are different when seeds are different
    assert not results_df1.equals(results_df2)

def test_task_func_no_penalties():
    # Test with no penalties
    rng_seed = 42
    goals = 5
    penalties = 0

    # Call the function
    results_df, _ = task_func(goals, penalties, rng_seed)

    # Check if all penalty costs are zero
    assert (results_df['Penalty Cost'] == 0).all()

def test_task_func_no_goals():
    # Test with no goals
    rng_seed = 42
    goals = 0
    penalties = 3

    # Call the function
    results_df, _ = task_func(goals, penalties, rng_seed)

    # Check if all goals are zero
    assert (results_df['Goals'] == 0).all()