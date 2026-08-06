import pytest
from src_0871 import task_func

def test_task_func():
    # Test case 1: Test that the function returns a DataFrame with the correct shape
    data_list = [('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]
    expected_shape = (5, 1)
    result = task_func(data_list)
    assert result.shape == expected_shape

    # Test case 2: Test that the function returns the correct mean values
    expected_mean_values = [2.1, 3.2, 4.3, 5.4, 6.5]
    result = task_func(data_list)
    assert result['Mean Value'].tolist() == expected_mean_values

    # Test case 3: Test that the function handles missing values correctly
    data_list = [('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5), ('f', np.nan, np.nan)]
    expected_mean_values = [2.1, 3.2, 4.3, 5.4, 6.5, np.nan]
    result = task_func(data_list)
    assert result['Mean Value'].tolist() == expected_mean_values