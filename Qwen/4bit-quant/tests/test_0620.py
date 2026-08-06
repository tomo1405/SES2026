import pandas as pd
import pytest
from src_0620 import task_func


def test_task_func():
    # Test with default parameters
    results_df, model = task_func(5, 3)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5  # Number of teams
    assert all(col in results_df.columns for col in ['Team', 'Goals', 'Penalty Cost'])
    
    # Check if the model is trained
    assert hasattr(model, 'coef_')
    assert hasattr(model, 'intercept_')

def test_task_func_with_seed():
    # Test with a fixed seed to ensure reproducibility
    results_df1, _ = task_func(5, 3, rng_seed=42)
    results_df2, _ = task_func(5, 3, rng_seed=42)
    assert results_df1.equals(results_df2)

def test_task_func_no_penalties():
    # Test when no penalties are possible
    results_df, _ = task_func(5, 0)
    assert (results_df['Penalty Cost'] == 0).all()

def test_task_func_max_penalties():
    # Test when maximum penalties are considered
    results_df, _ = task_func(5, 3)
    assert (results_df['Penalty Cost'] <= 3000).all()  # Maximum penalty cost is 3 * 1000

def test_task_func_no_teams():
    # Test with an empty list of teams
    original_teams = list(TEAMS)
    TEAMS.clear()
    with pytest.raises(ValueError):
        task_func(5, 3)
    TEAMS.extend(original_teams)  # Restore original state

def test_task_func_invalid_input():
    # Test with invalid input types
    with pytest.raises(TypeError):
        task_func('a', 3)
    with pytest.raises(TypeError):
        task_func(5, 'b')
    with pytest.raises(TypeError):
        task_func(5, 3, rng_seed='c')