python
import pandas as pd
import pytest
from src_0365 import task_func

# Constants
FEATURES = ['feature '+str(i) for i in range(1, 11)]
TARGET = 'target'

# Test case 1: Valid input DataFrame
def test_valid_input_df():
    df = pd.DataFrame({
        FEATURES[0]: [1, 2, 3, 4, 5],
        FEATURES[1]: [6, 7, 8, 9, 10],
        FEATURES[2]: [11, 12, 13, 14, 15],
        FEATURES[3]: [16, 17, 18, 19, 20],
        FEATURES[4]: [21, 22, 23, 24, 25],
        FEATURES[5]: [26, 27, 28, 29, 30],
        FEATURES[6]: [31, 32, 33, 34, 35],
        FEATURES[7]: [36, 37, 38, 39, 40],
        FEATURES[8]: [41, 42, 43, 44, 45],
        FEATURES[9]: [46, 47, 48, 49, 50],
        TARGET: [51, 52, 53, 54, 55]
    })
    model = task_func(df)
    assert isinstance(model, LinearRegression)

# Test case 2: Invalid input DataFrame
def test_invalid_input_df():
    df = 'not a DataFrame'
    with pytest.raises(ValueError):
        task_func(df)