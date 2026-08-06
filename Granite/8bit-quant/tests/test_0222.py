import pandas as pd
from src_0222 import task_func

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']

# Sample input data
df = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [5, 4, 3, 2, 1],
    'feature3': [10, 20, 30, 40, 50],
    'feature4': [50, 40, 30, 20, 10],
    'feature5': [100, 200, 300, 400, 500]
})
dct = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500}

# Expected output data
expected_statistics = {
    'feature1': {'mean': 250.0, 'median': 250.0, 'mode': 200.0, 'variance': 25000.0},
    'feature2': {'mean': 250.0, 'median': 250.0, 'mode': 200.0, 'variance': 25000.0},
    'feature3': {'mean': 300.0, 'median': 300.0, 'mode': 300.0, 'variance': 25000.0},
    'feature4': {'mean': 300.0, 'median': 300.0, 'mode': 300.0, 'variance': 25000.0},
    'feature5': {'mean': 300.0, 'median': 300.0, 'mode': 300.0, 'variance': 25000.0}
}

def test_task_func():
    # Test with valid input data
    result = task_func(df, dct)
    assert result == expected_statistics

    # Test with invalid input data
    invalid_df = pd.DataFrame({
        'feature1': ['a', 'b', 'c', 'd', 'e'],
        'feature2': ['e', 'd', 'c', 'b', 'a'],
        'feature3': [10, 20, 30, 40, 50],
        'feature4': [50, 40, 30, 20, 10],
        'feature5': [100, 200, 300, 400, 500]
    })
    result = task_func(invalid_df, dct)
    assert result == "Invalid input"