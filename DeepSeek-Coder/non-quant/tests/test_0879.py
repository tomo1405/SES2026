import pytest
from src_0879 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Define test cases
def test_task_func():
    # Test case 1: Basic functionality
    data = pd.DataFrame({
        'feature1': [1, 2, 3],
        'target': [10, 20, 30]
    })
    target = 'target'
    mse, model, _ = task_func(data, target)
    assert isinstance(mse, float), "The mean squared error should be a float."
    assert mse >= 0, "The mean squared error should be non-negative."

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()