import numpy as np
import pytest
from src_0158 import task_func


def test_task_func_input_validation():
    # Test with non-2D input
    with pytest.raises(ValueError, match="Input data must be a 2D numpy array."):
        task_func([1, 2, 3])

    # Test with 1D numpy array
    with pytest.raises(ValueError, match="Input data must be a 2D numpy array."):
        task_func(np.array([1, 2, 3]))

def test_task_func_correct_output():
    # Test with valid 2D numpy array
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df, ax = task_func(data)

    # Check if the DataFrame is correct
    expected_df = pd.DataFrame({
        0: [1, 4, 7],
        1: [2, 5, 8],
        2: [3, 6, 9],
        'Average': [2.0, 5.0, 8.0]
    })
    pd.testing.assert_frame_equal(df, expected_df)

    # Check if the heatmap axis is returned
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_empty_array():
    # Test with an empty 2D numpy array
    data = np.array([])
    with pytest.raises(ValueError, match="Input data must be a 2D numpy array."):
        task_func(data)