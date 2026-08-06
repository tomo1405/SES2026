import pytest
from src_0519 import task_func

def test_task_func():
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_df = pd.DataFrame(array, columns=['A', 'B', 'C'])
    expected_distance_matrix = pd.DataFrame(
        [[0.0, 1.0, 1.41421356],
         [1.0, 0.0, 1.41421356],
         [1.41421356, 1.41421356, 0.0]],
        index=['A', 'B', 'C'],
        columns=['A', 'B', 'C']
    )
    df, distance_matrix = task_func(array)
    assert df.equals(expected_df)
    assert distance_matrix.equals(expected_distance_matrix)

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func([[1, 2], [3, 4], [5]])
    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5], [6, 7, 8]])
    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5, 6], [7, 8, 'nine']])