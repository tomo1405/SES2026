import pytest
from src_0248 import task_func

def test_task_func_default_parameters():
    result = task_func()
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (N_DATA_POINTS, 1)
    assert 'Normalized Value' in result.columns

def test_task_func_custom_parameters():
    n_data_points = 1000
    min_value = 1.0
    max_value = 5.0
    result = task_func(n_data_points, min_value, max_value)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (n_data_points, 1)
    assert 'Normalized Value' in result.columns

def test_task_func_min_greater_than_max():
    with pytest.raises(ValueError):
        task_func(max_value=0.0, min_value=1.0)

def test_task_func_min_equal_to_max():
    result = task_func(min_value=5.0, max_value=5.0)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (N_DATA_POINTS, 1)
    assert 'Normalized Value' in result.columns
    assert all(result['Normalized Value'] == 0.0)

def test_task_func_data_distribution():
    result = task_func()
    mean = result['Normalized Value'].mean()
    std_dev = result['Normalized Value'].std()
    assert abs(mean) < 1e-6, f"Mean is not close to 0: {mean}"
    assert abs(std_dev - 1.0) < 1e-6, f"Standard deviation is not close to 1: {std_dev}"