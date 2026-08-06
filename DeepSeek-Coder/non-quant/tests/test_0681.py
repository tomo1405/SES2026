import pytest
from src_0681 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Test cases for the task_func function
def test_task_func():
    # Create a sample DataFrame
    data = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'feature3': [7, 8, 9]
    }
    df = pd.DataFrame(data)
    
    # Test with no features to scale
    result = task_func(df, [])
    assert df.equals(result)

    # Test with features to scale
    features_to_scale = ['feature1', 'feature2']
    result = task_func(df, features_to_scale)
    assert result.equals(df[['feature1', 'feature2']])

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()