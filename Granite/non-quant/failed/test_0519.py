import pytest
from src_0519 import task_func

def test_task_func_valid_input():
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    df, distance_matrix = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(distance_matrix, pd.DataFrame)

def test_task_func_invalid_input_type():
    with pytest.raises(TypeError):
        task_func("invalid input")

def test_task_func_invalid_sublist_type():
    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, "5", 6], [7, 8, 9]])

def test_task_func_invalid_element_type():
    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5, 6.0], [7, 8, 9]])