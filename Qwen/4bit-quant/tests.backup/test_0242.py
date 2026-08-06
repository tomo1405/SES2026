import pytest
from src_0242 import task_func
import numpy as np

def test_task_func_with_non_empty_input():
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    
    # Check if the arrays are of the same shape
    assert arr.shape == norm_arr.shape
    
    # Check if the original array is correctly formed
    assert np.array_equal(arr, np.array([2, 4, 6]))
    
    # Check if the normalized array has values between 0 and 1
    assert np.all(norm_arr >= 0) and np.all(norm_arr <= 1)

def test_task_func_with_empty_input():
    original = []
    arr, norm_arr, ax = task_func(original)
    
    # Check if both arrays are empty
    assert arr.size == 0 and norm_arr.size == 0

def test_task_func_with_single_element_input():
    original = [(1, 1)]
    arr, norm_arr, ax = task_func(original)
    
    # Check if the arrays are of the same shape
    assert arr.shape == norm_arr.shape
    
    # Check if the original array is correctly formed
    assert np.array_equal(arr, np.array([1]))
    
    # Check if the normalized array is the same as the original
    assert np.array_equal(norm_arr, arr)

def test_task_func_with_negative_values():
    original = [(-1, -2), (-3, -4), (-5, -6)]
    arr, norm_arr, ax = task_func(original)
    
    # Check if the arrays are of the same shape
    assert arr.shape == norm_arr.shape
    
    # Check if the original array is correctly formed
    assert np.array_equal(arr, np.array([-2, -4, -6]))
    
    # Check if the normalized array has values between 0 and 1
    assert np.all(norm_arr >= 0) and np.all(norm_arr <= 1)