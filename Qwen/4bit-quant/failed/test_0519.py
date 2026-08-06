import pytest
from src_0519 import task_func
import numpy as np

def test_task_func_input_type():
    with pytest.raises(TypeError, match="Input must be a list."):
        task_func(123)

def test_task_func_sublist_type():
    with pytest.raises(TypeError, match="Input must be a list of lists."):
        task_func([1, 2, 3])

def test_task_func_element_type():
    with pytest.raises(TypeError, match="All elements in the sublists must be int or float."):
        task_func([[1, 2], ['a', 3]])

def test_task_func_correct_output():
    input_data = [[1, 2], [4, 6], [7, 8]]
    df, distance_matrix = task_func(input_data)
    
    expected_df = pd.DataFrame({
        'A': [1, 4, 7],
        'B': [2, 6, 8]
    })
    
    expected_distances = np.array([
        [0., 5., 7.07106781],
        [5., 0., 5.],
        [7.07106781, 5., 0.]
    ])
    
    pd.testing.assert_frame_equal(df, expected_df)
    np.testing.assert_almost_equal(distance_matrix.values, expected_distances)

def test_task_func_single_element():
    input_data = [[1]]
    df, distance_matrix = task_func(input_data)
    
    expected_df = pd.DataFrame({
        'A': [1]
    })
    
    expected_distances = np.array([[0.]])
    
    pd.testing.assert_frame_equal(df, expected_df)
    np.testing.assert_almost_equal(distance_matrix.values, expected_distances)