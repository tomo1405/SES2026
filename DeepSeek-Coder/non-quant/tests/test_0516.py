import pytest
from src_0516 import task_func
import pandas as pd
import seaborn as sns

def test_task_func():
    # Test case 1: Valid input
    array = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
    expected_df = pd.DataFrame({
        "A": [1, 5],
        "B": [2, 4],
        "C": [3, 3],
        "D": [4, 2],
        "E": [5, 1]
    })
    expected_heatmap = None  # Heatmap is not returned directly, so we don't check it

    result_df, result_heatmap = task_func(array)
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Add more test cases as needed

if __name__ == "__main__":
    pytest.main()