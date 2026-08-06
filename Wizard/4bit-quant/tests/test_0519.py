python
import pandas as pd
import pytest
from scipy.spatial.distance import pdist, squareform

def task_func(array):
    if not isinstance(array, list):
        raise TypeError("Input must be a list.")

    if not all(isinstance(sublist, list) for sublist in array):
        raise TypeError("Input must be a list of lists.")

    for sublist in array:
        if not all(isinstance(item, (int, float)) for item in sublist):
            raise TypeError("All elements in the sublists must be int or float.")

    columns = [chr(65 + i) for i in range(len(array[0]))]
    df = pd.DataFrame(array, columns=columns)

    distances = pdist(df.values, metric="euclidean")
    distance_matrix = pd.DataFrame(
        squareform(distances), index=df.index, columns=df.index
    )

    return df, distance_matrix

def test_task_func():
    # Test case 1: Valid input
    array = [[1, 2, 3], [4, 5, 6]]
    expected_df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
    expected_distance_matrix = pd.DataFrame([[0.0, 2.8284271247461903, 5.656854249492381],
                                            [2.8284271247461903, 0.0, 2.8284271247461903],
                                            [5.656854249492381, 2.8284271247461903, 0.0]],
                                           index=['A', 'B', 'C'], columns=['A', 'B', 'C'])
    df, distance_matrix = task_func(array)
    assert df.equals(expected_df)
    assert distance_matrix.equals(expected_distance_matrix)

    # Test case 2: Invalid input type
    with pytest.raises(TypeError):
        task_func("not a list")

    # Test case 3: Invalid sublist type
    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5, "6"]])

    # Test case 4: Invalid element type
    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5, []]])