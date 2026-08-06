import pytest
from src_0916 import task_func

def test_task_func():
    # Mock input data
    df = {'closing_price': [1, 2, 3, 4, 5]}
    
    # Call the function with the mock data
    outliers, ax = task_func(df)
    
    # Assert the expected output
    assert len(outliers) == 0  # No outliers expected with a threshold of 2
    
    # Change the input data to include an outlier
    df['closing_price'].append(100)
    
    # Call the function again with the updated data
    outliers, ax = task_func(df)
    
    # Assert that the expected outlier is present
    assert len(outliers) == 1
    assert outliers.iloc[0]['closing_price'] == 100