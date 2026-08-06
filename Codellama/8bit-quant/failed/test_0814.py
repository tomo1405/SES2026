import pytest
from src_0814 import task_func

def test_task_func():
    number_list = [1, 2, 3, 4, 5]
    element = 6
    expected_result = pd.DataFrame({'Combinations': [[1, 2, 3], [2, 3, 4], [3, 4, 5]]})
    result = task_func(number_list, element)
    assert result.equals(expected_result)