import pytest
from src_0759 import task_func

def test_task_func():
    # Test that the function returns a pandas DataFrame
    demographics = task_func(10)
    assert isinstance(demographics, pd.DataFrame)

    # Test that the function raises a ValueError if num_samples is not an integer
    with pytest.raises(ValueError):
        task_func(10.5)

    # Test that the function returns the correct number of rows
    demographics = task_func(10)
    assert len(demographics) == 10

    # Test that the function returns the correct number of columns
    demographics = task_func(10)
    assert len(demographics.columns) == 3

    # Test that the function returns the correct column names
    demographics = task_func(10)
    assert list(demographics.columns) == ['Country', 'Age', 'Gender']

    # Test that the function returns the correct data types
    demographics = task_func(10)
    assert demographics['Country'].dtype == object
    assert demographics['Age'].dtype == np.int64
    assert demographics['Gender'].dtype == np.int64

    # Test that the function returns the correct data values
    demographics = task_func(10)
    assert demographics['Country'].unique() == ['Russia', 'China', 'USA', 'India', 'Brazil']
    assert demographics['Age'].min() == 18
    assert demographics['Age'].max() == 59
    assert demographics['Gender'].unique() == ['Male', 'Female']