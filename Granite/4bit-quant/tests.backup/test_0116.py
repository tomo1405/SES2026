import pytest
from src_0116 import task_func

def test_task_func():
    numbers = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
    expected_result = {'array': np.array([1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]),
                       'mode': 4,
                       'entropy': 2.321928094887362}
    result = task_func(numbers)
    assert result == expected_result

def test_task_func_with_empty_list():
    numbers = []
    with pytest.raises(ValueError):
        task_func(numbers)