import pytest
from src_0785 import task_func

def test_task_func():
    # Test case 1: Test the function with n=10 and random_seed=42
    df = task_func(n=10, random_seed=42)
    assert df.shape == (10, 4)  # Check if the resulting DataFrame has the correct shape
    assert df['Site'].nunique() == 5  # Check if the number of unique sites is 5
    assert df['Category'].nunique() == 5  # Check if the number of unique categories is 5
    assert df['Response'].nunique() == 5  # Check if the number of unique responses is 5
    assert df['Value'].min() == 1  # Check if the minimum value of 'Value' is 1
    assert df['Value'].max() == 5  # Check if the maximum value of 'Value' is 5

    # Test case 2: Test the function with n=50 and random_seed=None
    df = task_func(n=50)
    assert df.shape == (50, 4)  # Check if the resulting DataFrame has the correct shape
    assert df['Site'].nunique() == 5  # Check if the number of unique sites is 5
    assert df['Category'].nunique() == 5  # Check if the number of unique categories is 5
    assert df['Response'].nunique() == 5  # Check if the number of unique responses is 5
    assert df['Value'].min() == 1  # Check if the minimum value of 'Value' is 1
    assert df['Value'].max() == 5  # Check if the maximum value of 'Value' is 5

if __name__ == "__main__":
    pytest.main()