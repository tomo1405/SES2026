import pytest
from src_0172 import task_func
import pandas as pd

def test_task_func():
    # Test with a simple dictionary
    vegetable_dict = {'a': 'Carrot', 'b': 'Potato', 'c': 'Tomato'}
    result_df = task_func(vegetable_dict, seed=42)

    # Check if the DataFrame has the correct shape
    assert result_df.shape == (3, 2), "The DataFrame should have 3 rows and 2 columns."

    # Check if the 'Count' column is within the expected range
    assert all(result_df['Count'] >= 1) and all(result_df['Count'] <= 10), "Counts should be between 1 and 10."

    # Check if the 'Percentage' column sums to 100%
    assert abs(result_df['Percentage'].sum() - 100) < 1e-6, "The sum of percentages should be 100%."

    # Test with an empty dictionary
    empty_dict = {}
    empty_result_df = task_func(empty_dict, seed=42)
    assert empty_result_df.empty, "The DataFrame should be empty for an empty input dictionary."

    # Test with a dictionary containing only keys not in VEGETABLES
    invalid_vegetable_dict = {'d': 'Broccoli', 'e': 'Lettuce'}
    invalid_result_df = task_func(invalid_vegetable_dict, seed=42)
    assert invalid_result_df.empty, "The DataFrame should be empty for a dictionary with invalid vegetable names."

    # Test with a dictionary containing duplicate values
    duplicate_vegetable_dict = {'f': 'Carrot', 'g': 'Carrot'}
    duplicate_result_df = task_func(duplicate_vegetable_dict, seed=42)
    assert duplicate_result_df.shape == (1, 2), "The DataFrame should have 1 row for duplicate values."
    assert duplicate_result_df.index[0] == 'Carrot', "The index should be 'Carrot' for duplicate values."

# Run the tests
if __name__ == "__main__":
    pytest.main()