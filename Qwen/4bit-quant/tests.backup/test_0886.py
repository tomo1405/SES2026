import pytest
from src_0886 import task_func
import pandas as pd
import numpy as np

# Mocking the LinearRegression predict method to avoid actual model training
class MockLinearRegression:
    def fit(self, X, y):
        pass

    def predict(self, X):
        return np.array([100, 200, 300])  # Example predictions

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [55, 60, 70, 80, 90],
        'C': [900, 900, 900, 900, 900]
    }
    return pd.DataFrame(data)

def test_task_func_with_valid_data(sample_df):
    # Replace the actual LinearRegression with the mock class
    original_LinearRegression = task_func.LinearRegression
    task_func.LinearRegression = MockLinearRegression

    result = task_func(sample_df)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], np.ndarray)
    assert isinstance(result[1], MockLinearRegression)

    # Restore the original LinearRegression class
    task_func.LinearRegression = original_LinearRegression

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    result = task_func(df)
    assert result is None

def test_task_func_with_missing_columns(sample_df):
    df = sample_df.drop(columns=['A'])
    result = task_func(df)
    assert result is None

def test_task_func_with_non_numeric_data(sample_df):
    sample_df['A'] = ['a', 'b', 'c', 'd', 'e']
    result = task_func(sample_df)
    assert result is None

def test_task_func_with_no_data_selected(sample_df):
    sample_df['B'] = [40, 45, 50, 55, 60]
    result = task_func(sample_df)
    assert result is None

def test_task_func_with_seed(sample_df):
    # Replace the actual LinearRegression with the mock class
    original_LinearRegression = task_func.LinearRegression
    task_func.LinearRegression = MockLinearRegression

    result = task_func(sample_df, seed=42)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], np.ndarray)
    assert isinstance(result[1], MockLinearRegression)

    # Restore the original LinearRegression class
    task_func.LinearRegression = original_LinearRegression