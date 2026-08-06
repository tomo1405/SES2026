import pytest
from src_0626 import task_func

def test_task_func():
    # Test case 1: Check if the function returns a DataFrame
    cities_list = ['City1', 'City2', 'City3']
    result = task_func(cities_list=cities_list)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"

    # Add more test cases as needed

# Add more test cases as needed