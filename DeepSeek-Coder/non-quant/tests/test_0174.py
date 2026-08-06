import pytest
from src_0174 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Create a sample input dictionary
    country_dict = {
        'USA': 'USA',
        'UK': 'UK',
        'China': 'China',
        'Japan': 'Japan',
        'Australia': 'Australia'
    }

    # Call the function with the sample input
    result = task_func(country_dict)

    # Check the output
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert not result.empty, "The DataFrame should not be empty"
    assert set(result.index) == set(country_dict.values()), "The index should match the countries"
    assert all(result['GDP'] > 1000000000), "All GDP values should be greater than 1 billion"