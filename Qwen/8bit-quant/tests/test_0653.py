import pytest
from src_0653 import task_func
import numpy as np
import matplotlib.pyplot as plt
import io
import sys

# Mocking plt.show to prevent actual plotting during tests
@pytest.fixture(autouse=True)
def mock_plt_show(monkeypatch):
    def mock_show():
        pass
    monkeypatch.setattr(plt, 'show', mock_show)

def test_task_func_no_data():
    # Test case when there is no data matching the target value
    array = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['33', '33', '2'], ['33', '22', '332']])
    result = task_func(target_value='999', array=array)
    assert result == ('N/A', 'N/A', 'N/A', 'N/A')

def test_task_func_one_match():
    # Test case when there is only one match for the target value
    array = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
    result = task_func(target_value='332', array=array)
    assert result == (2.0, 'N/A', 'N/A', 'N/A')

def test_task_func_multiple_matches():
    # Test case when there are multiple matches for the target value
    array = np.array([['0', '1', '2'], ['332', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
    result = task_func(target_value='332', array=array)
    assert isinstance(result, tuple)
    assert len(result) == 4
    mean, variance, skewness, kurtosis = result
    assert isinstance(mean, float)
    assert isinstance(variance, float)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)

def test_task_func_default_values():
    # Test case using default values
    result = task_func()
    assert isinstance(result, tuple)
    assert len(result) == 4
    mean, variance, skewness, kurtosis = result
    assert isinstance(mean, float)
    assert isinstance(variance, float)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)

def test_task_func_empty_array():
    # Test case with an empty array
    array = np.array([])
    result = task_func(array=array)
    assert result == ('N/A', 'N/A', 'N/A', 'N/A')

def test_task_func_non_string_target_value():
    # Test case with a non-string target value
    array = np.array([['0', '1', '2'], ['332', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
    with pytest.raises(TypeError):
        task_func(target_value=332, array=array)

def test_task_func_non_array_input():
    # Test case with a non-array input
    with pytest.raises(IndexError):
        task_func(array=[['0', '1', '2'], ['332', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])