import pandas as pd
import pytest
from src_0519 import task_func


def test_task_func():
    # Test 1: Input is not a list
    with pytest.raises(TypeError):
        task_func(1)

    # Test 2: Input is not a list of lists
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

    # Test 3: Input is a list of lists, but not all elements are int or float
    with pytest.raises(TypeError):
        task_func([[1, 2], [3, "a"]])

    # Test 4: Input is a valid list of lists
    array = [[1, 2], [3, 4]]
    df, distance_matrix = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(distance_matrix, pd.DataFrame)
    assert df.shape == (2, 2)
    assert distance_matrix.shape == (2, 2)

    # Test 5: Input is a valid list of lists, but with different lengths
    array = [[1, 2], [3, 4, 5]]
    df, distance_matrix = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(distance_matrix, pd.DataFrame)
    assert df.shape == (2, 3)
    assert distance_matrix.shape == (2, 2)

    # Test 6: Input is a valid list of lists, but with different types
    array = [[1, 2], [3.0, 4.0]]
    df, distance_matrix = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(distance_matrix, pd.DataFrame)
    assert df.shape == (2, 2)
    assert distance_matrix.shape == (2, 2)