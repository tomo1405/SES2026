import pytest
from src_0519 import task_func

def test_task_func_valid_input():
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    df, distance_matrix = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(distance_matrix, pd.DataFrame)

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func("not a list")
    with pytest.raises(TypeError):
        task_func([[1, 2], [3, 4], [5]])
    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5, "six"], [7, 8, 9]])