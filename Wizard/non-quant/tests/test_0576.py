python
import pytest
from src_0576 import task_func

def test_task_func():
    # Test case 1
    l = [1, 2, 3, 4, 5]
    n_groups = 2
    expected_result = pd.DataFrame([[4, 5, 1, 2], [3, 4, 5, 1]])
    result = task_func(l, n_groups)
    assert result.equals(expected_result)

    # Test case 2
    l = []
    n_groups = 5
    expected_result = pd.DataFrame()
    result = task_func(l, n_groups)
    assert result.equals(expected_result)

    # Test case 3
    l = [1, 2, 3, 4, 5]
    n_groups = 10
    expected_result = pd.DataFrame([[5, 1, 2, 3, 4, 5, 1, 2, 3, 4], [4, 5, 1, 2, 3, 4, 5, 1, 2, 3]])
    result = task_func(l, n_groups)
    assert result.equals(expected_result)