python
import pytest
from src_0576 import task_func

def test_task_func():
    # Test case 1
    l = [1, 2, 3, 4, 5]
    n_groups = 2
    expected_df = pd.DataFrame([[5, 4], [3, 2], [1, 0]])
    actual_df = task_func(l, n_groups)
    assert actual_df.equals(expected_df)

    # Test case 2
    l = []
    n_groups = 5
    expected_df = pd.DataFrame()
    actual_df = task_func(l, n_groups)
    assert actual_df.equals(expected_df)

    # Test case 3
    l = [1, 2, 3, 4, 5]
    n_groups = 10
    expected_df = pd.DataFrame([[5, 4, 3, 2, 1, 0, 0, 0, 0, 0], [4, 3, 2, 1, 0, 0, 0, 0, 0, 0], [3, 2, 1, 0, 0, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    actual_df = task_func(l, n_groups)
    assert actual_df.equals(expected_df)