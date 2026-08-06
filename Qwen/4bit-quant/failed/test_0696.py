import pytest
from src_0696 import task_func
import numpy as np
from sklearn.decomposition import PCA

def test_task_func_with_default_n_components():
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    n_components = 2
    expected_output = np.array([[1., 2.],
                                [3., 4.],
                                [5., 6.]])
    
    result = task_func(tuples_list, n_components)
    
    assert np.allclose(result, expected_output), "The result does not match the expected output."

def test_task_func_with_reduced_dimensions():
    tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    n_components = 2
    pca = PCA(n_components=n_components)
    data = np.array(tuples_list)
    expected_output = pca.fit_transform(data)
    
    result = task_func(tuples_list, n_components)
    
    assert np.allclose(result, expected_output), "The result does not match the expected output."

def test_task_func_with_single_component():
    tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    n_components = 1
    pca = PCA(n_components=n_components)
    data = np.array(tuples_list)
    expected_output = pca.fit_transform(data)
    
    result = task_func(tuples_list, n_components)
    
    assert np.allclose(result, expected_output), "The result does not match the expected output."

def test_task_func_with_more_components_than_features():
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    n_components = 3
    with pytest.raises(ValueError) as excinfo:
        task_func(tuples_list, n_components)
    
    assert "n_components=3 must be between 0 and min(n_samples, n_features)=2 with svd_solver='full'" in str(excinfo.value), "The exception message does not match the expected error."

def test_task_func_with_empty_input():
    tuples_list = []
    n_components = 2
    expected_output = np.array([])
    
    result = task_func(tuples_list, n_components)
    
    assert np.array_equal(result, expected_output), "The result does not match the expected output."