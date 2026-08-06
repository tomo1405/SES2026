import pytest
from src_0698 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'feature': [1, 2, 3, 4, 5],
        'value': [2, 4, 6, 8, 10]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    result = task_func(sample_data)
    expected_coefficients = [[2.0]]
    expected_intercept = [0.0]
    
    assert result['coefficients'] == expected_coefficients, f"Expected coefficients {expected_coefficients}, but got {result['coefficients']}"
    assert result['intercept'] == expected_intercept, f"Expected intercept {expected_intercept}, but got {result['intercept']}"

def test_task_func_with_negative_values(sample_data):
    sample_data['value'] = [-2, -4, -6, -8, -10]
    result = task_func(sample_data)
    expected_coefficients = [[-2.0]]
    expected_intercept = [0.0]
    
    assert result['coefficients'] == expected_coefficients, f"Expected coefficients {expected_coefficients}, but got {result['coefficients']}"
    assert result['intercept'] == expected_intercept, f"Expected intercept {expected_intercept}, but got {result['intercept']}"

def test_task_func_with_zero_values(sample_data):
    sample_data['value'] = [0, 0, 0, 0, 0]
    result = task_func(sample_data)
    expected_coefficients = [[0.0]]
    expected_intercept = [0.0]
    
    assert result['coefficients'] == expected_coefficients, f"Expected coefficients {expected_coefficients}, but got {result['coefficients']}"
    assert result['intercept'] == expected_intercept, f"Expected intercept {expected_intercept}, but got {result['intercept']}"

def test_task_func_with_random_values(sample_data):
    np.random.seed(0)
    sample_data['value'] = np.random.rand(5)
    result = task_func(sample_data)
    expected_coefficients = [[0.49671415]]
    expected_intercept = [0.0]
    
    assert np.allclose(result['coefficients'], expected_coefficients), f"Expected coefficients {expected_coefficients}, but got {result['coefficients']}"
    assert np.isclose(result['intercept'][0], expected_intercept[0]), f"Expected intercept {expected_intercept}, but got {result['intercept']}"