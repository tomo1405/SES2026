import pytest
from src_0702 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func():
    # Create a sample DataFrame
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)
    
    # Call the function with the DataFrame and target column
    score = task_func(df, 'target')
    
    # Assert that the score is a float
    assert isinstance(score, float)
    
    # Assert that the score is between 0 and 1 (inclusive)
    assert 0 <= score <= 1
    
    # Additional test case with different data
    data2 = {
        'feature1': [10, 20, 30, 40, 50],
        'feature2': [50, 40, 30, 20, 10],
        'target': [100, 200, 300, 400, 500]
    }
    df2 = pd.DataFrame(data2)
    
    score2 = task_func(df2, 'target')
    
    assert isinstance(score2, float)
    assert 0 <= score2 <= 1

# Run the tests
if __name__ == "__main__":
    pytest.main()