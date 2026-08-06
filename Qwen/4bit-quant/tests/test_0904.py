import pytest
from src_0904 import task_func


@pytest.fixture
def sample_data():
    data = {
        'x1': [1, 2, 3, 4],
        'x2': [5, 6, 7, 8],
        'z': [9, 10, 11, 12]
    }
    return data

def test_task_func_with_valid_data(sample_data):
    model = task_func(sample_data)
    assert isinstance(model, LinearRegression)
    assert hasattr(model, 'coef_')
    assert hasattr(model, 'intercept_')

def test_task_func_with_single_predictor(sample_data):
    del sample_data['x2']
    model = task_func(sample_data)
    assert isinstance(model, LinearRegression)
    assert len(model.coef_) == 1

def test_task_func_with_no_predictors():
    data = {'z': [1, 2, 3, 4]}
    with pytest.raises(KeyError):
        task_func(data)

def test_task_func_with_empty_data():
    data = {}
    with pytest.raises(KeyError):
        task_func(data)

def test_task_func_with_non_numeric_target(sample_data):
    sample_data['z'] = ['a', 'b', 'c', 'd']
    with pytest.raises(ValueError):
        task_func(sample_data)

def test_task_func_with_non_numeric_predictor(sample_data):
    sample_data['x1'] = ['a', 'b', 'c', 'd']
    with pytest.raises(ValueError):
        task_func(sample_data)