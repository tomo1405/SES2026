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
    assert isinstance(result, dict)
    assert 'coefficients' in result
    assert 'intercept' in result
    assert isinstance(result['coefficients'], list)
    assert isinstance(result['intercept'], list)
    assert len(result['coefficients']) == 1
    assert len(result['intercept']) == 1
    assert np.isclose(result['coefficients'][0], 2.0)
    assert np.isclose(result['intercept'][0], 0.0)

def test_task_func_with_random_data():
    np.random.seed(0)
    data = {
        'feature': np.random.rand(10),
        'value': np.random.rand(10) * 10
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, dict)
    assert 'coefficients' in result
    assert 'intercept' in result
    assert isinstance(result['coefficients'], list)
    assert isinstance(result['intercept'], list)
    assert len(result['coefficients']) == 1
    assert len(result['intercept']) == 1

def test_task_func_with_single_point():
    data = {
        'feature': [1],
        'value': [2]
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, dict)
    assert 'coefficients' in result
    assert 'intercept' in result
    assert isinstance(result['coefficients'], list)
    assert isinstance(result['intercept'], list)
    assert len(result['coefficients']) == 1
    assert len(result['intercept']) == 1
    assert np.isclose(result['coefficients'][0], 0.0)
    assert np.isclose(result['intercept'][0], 2.0)