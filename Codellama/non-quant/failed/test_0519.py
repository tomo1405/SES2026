import pytest
from src_0519 import task_func

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func(1)

def test_task_func_input_value():
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

def test_task_func_input_sublist_type():
    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]])

def test_task_func_input_sublist_value():
    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

def test_task_func_output_type():
    df, distance_matrix = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert isinstance(df, pd.DataFrame)
    assert isinstance(distance_matrix, pd.DataFrame)

def test_task_func_output_value():
    df, distance_matrix = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert df.shape == (3, 3)
    assert distance_matrix.shape == (3, 3)