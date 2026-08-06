python
import pytest
from src_0519 import task_func

def test_task_func():
    # Test valid input
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    df, distance_matrix = task_func(array)
    assert df.shape == (3, 3)
    assert distance_matrix.shape == (3, 3)
    assert df.columns.tolist() == ['A', 'B', 'C']
    assert df.index.tolist() == [0, 1, 2]
    assert distance_matrix.index.tolist() == [0, 1, 2]
    assert distance_matrix.columns.tolist() == [0, 1, 2]
    assert distance_matrix.values.tolist() == [
        [0.0, 2.8284271247461903, 5.656854249492381],
        [2.8284271247461903, 0.0, 2.8284271247461903],
        [5.656854249492381, 2.8284271247461903, 0.0],
    ]

    # Test invalid input
    with pytest.raises(TypeError):
        task_func("not a list")

    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5, "6"], [7, 8, 9]])

    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5], [7, 8, 9]])

    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5, 6], [7, 8, "9"]])