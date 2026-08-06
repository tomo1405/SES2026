import pytest
from src_0154 import task_func
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def test_task_func():
    # Test data
    data = ['A', 'B', 'A', 'C', 'B']
    
    # Call the function
    result = task_func(data)
    
    # Check the output
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == len(data), "The DataFrame should have the same number of rows as the input data"
    assert set(result.columns) == {'Category', 'Encoded'}, "The DataFrame should have columns 'Category' and 'Encoded'"
    assert all(result['Category'] == data), "The 'Category' column should match the input data"
    assert all(result['Encoded'].isin([0, 1, 2])), "The 'Encoded' column should be encoded"

# Run the test
if __name__ == "__main__":
    pytest.main()