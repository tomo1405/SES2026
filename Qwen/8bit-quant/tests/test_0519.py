import pandas as pd
import pytest
from src_0519 import task_func


def test_task_func_with_valid_input():
    input_data = [[1, 2], [3, 4], [5, 6]]
    df, distance_matrix = task_func(input_data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(distance_matrix, pd.DataFrame)
    assert df.equals(pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A', 'B']))
    assert distance_matrix.equals(pd.DataFrame({
        0: [0.0, 2.828427, 5.656854],
        1: [2.828427, 0.0, 2.828427],
        2: [5.656854, 2.828427, 0.0]
    }, index=[0, 1, 2]))

def test_task_func_with_non_list_input():
    with pytest.raises(TypeError, match="Input must be a list."):
        task_func("not a list")

def test_task_func_with_non_list_of_lists_input():
    with pytest.raises(TypeError, match="Input must be a list of lists."):
        task_func([1, 2, 3])

def test_task_func_with_non_numeric_elements():
    with pytest.raises(TypeError, match="All elements in the sublists must be int or float."):
        task_func([[1, "a"], [3, 4]])

def test_task_func_with_empty_list():
    input_data = []
    df, distance_matrix = task_func(input_data)
    assert df.empty
    assert distance_matrix.empty

def test_task_func_with_single_element_sublists():
    input_data = [[1], [2], [3]]
    df, distance_matrix = task_func(input_data)
    assert df.equals(pd.DataFrame([[1], [2], [3]], columns=['A']))
    assert distance_matrix.equals(pd.DataFrame({
        0: [0.0, 1.0, 2.0],
        1: [1.0, 0.0, 1.0],
        2: [2.0, 1.0, 0.0]
    }, index=[0, 1, 2]))