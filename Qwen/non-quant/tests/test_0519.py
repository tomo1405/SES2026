import pytest
from src_0519 import task_func
import pandas as pd
import numpy as np

def test_task_func_input_type():
    with pytest.raises(TypeError, match="Input must be a list."):
        task_func("not a list")

def test_task_func_sublist_type():
    with pytest.raises(TypeError, match="Input must be a list of lists."):
        task_func([1, 2, 3])

def test_task_func_element_type():
    with pytest.raises(TypeError, match="All elements in the sublists must be int or float."):
        task_func([[1, 2], ['a', 4]])

def test_task_func_correct_output():
    input_data = [[1, 2], [3, 4]]
    df, distance_matrix = task_func(input_data)
    
    expected_df = pd.DataFrame({
        'A': [1, 3],
        'B': [2, 4]
    })
    
    expected_distance_matrix = pd.DataFrame({
        '0': [0.0, 2.828427],
        '1': [2.828427, 0.0]
    }, index=[0, 1])
    
    pd.testing.assert_frame_equal(df, expected_df)
    pd.testing.assert_frame_equal(distance_matrix, expected_distance_matrix)

def test_task_func_empty_list():
    input_data = []
    df, distance_matrix = task_func(input_data)
    
    expected_df = pd.DataFrame(columns=['A'])
    expected_distance_matrix = pd.DataFrame()
    
    pd.testing.assert_frame_equal(df, expected_df)
    pd.testing.assert_frame_equal(distance_matrix, expected_distance_matrix)

def test_task_func_single_element():
    input_data = [[1]]
    df, distance_matrix = task_func(input_data)
    
    expected_df = pd.DataFrame({
        'A': [1]
    })
    
    expected_distance_matrix = pd.DataFrame({
        '0': [0.0]
    }, index=[0])
    
    pd.testing.assert_frame_equal(df, expected_df)
    pd.testing.assert_frame_equal(distance_matrix, expected_distance_matrix)