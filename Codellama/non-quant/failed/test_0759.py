import pytest
from src_0759 import task_func

def test_task_func():
    # Test that the function returns a DataFrame
    demographics = task_func(10)
    assert isinstance(demographics, pd.DataFrame)

    # Test that the DataFrame has the correct columns
    expected_columns = ['Country', 'Age', 'Gender']
    assert all(col in demographics.columns for col in expected_columns)

    # Test that the DataFrame has the correct number of rows
    assert len(demographics) == 10

    # Test that the function raises a ValueError if num_samples is not an integer
    with pytest.raises(ValueError):
        task_func(1.5)

    # Test that the function raises a ValueError if countries is not a list
    with pytest.raises(ValueError):
        task_func(10, countries='Russia')

    # Test that the function raises a ValueError if ages is not a list
    with pytest.raises(ValueError):
        task_func(10, ages=18)

    # Test that the function raises a ValueError if genders is not a list
    with pytest.raises(ValueError):
        task_func(10, genders='Male')

    # Test that the function raises a ValueError if rng_seed is not an integer
    with pytest.raises(ValueError):
        task_func(10, rng_seed='random')