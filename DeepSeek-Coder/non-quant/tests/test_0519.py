import pytest
from src_0519 import task_func
import pandas as pd
from scipy.spatial.distance import pdist, squareform

def test_task_func():
    # Test case 1: Basic functionality
    array = [[1, 2], [3, 4]]
    expected_df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
    expected_distance_matrix = pd.DataFrame([[0, 2**0.5, 2**0.5, 4**0.5], [2**0.5, 0, 2**0.5, 2**0.5], [2**0.5, 2**0.5, 0, 2**0.5], [4**0.5, 2**0.5, 2**0.5, 0]])
    expected_distance_matrix = pd.DataFrame(squareform(expected_distance_matrix), index=expected_df.index, columns=expected_df.index)
    
    df, distance_matrix = task_func(array)
    pd.testing.assert_frame_equal(df, expected_df)
    pd.testing.assert_frame_equal(distance_matrix, expected_distance_matrix)

    # Add more test cases as needed

if __name__ == "__main__":
    pytest.main()