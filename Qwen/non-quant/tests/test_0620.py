from sklearn.linear_model import LinearRegression
from src_0620 import task_func


def test_task_func_output():
    goals = 5
    penalties = 3
    rng_seed = 42
    results_df, model = task_func(goals, penalties, rng_seed)

    # Check if the DataFrame has the correct shape
    assert results_df.shape == (5, 3), "DataFrame should have 5 rows and 3 columns"

    # Check if the DataFrame has the correct columns
    assert list(results_df.columns) == ['Team', 'Goals', 'Penalty Cost'], "DataFrame columns are incorrect"

    # Check if the DataFrame contains the correct teams
    assert all(team in TEAMS for team in results_df['Team']), "DataFrame should contain only valid teams"

    # Check if the model is an instance of LinearRegression
    assert isinstance(model, LinearRegression), "Model should be an instance of LinearRegression"

    # Check if the model coefficients are as expected
    expected_coefficients = [PENALTY_COST, 0]  # Intercept is 0 because we fit on Goals only
    assert all(abs(coef - exp_coef) < 1e-6 for coef, exp_coef in zip(model.coef_, expected_coefficients)), "Model coefficients are incorrect"

def test_task_func_randomness():
    goals = 5
    penalties = 3
    rng_seed = 42
    results_df1, _ = task_func(goals, penalties, rng_seed)
    results_df2, _ = task_func(goals, penalties, rng_seed)

    # Check if the results are reproducible with the same seed
    assert results_df1.equals(results_df2), "Results should be reproducible with the same seed"

def test_task_func_no_seed():
    goals = 5
    penalties = 3
    results_df1, _ = task_func(goals, penalties)
    results_df2, _ = task_func(goals, penalties)

    # Check if the results are different without a seed
    assert not results_df1.equals(results_df2), "Results should be different without a seed"