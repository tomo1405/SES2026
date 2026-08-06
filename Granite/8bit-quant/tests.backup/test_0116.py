import pytest
from src_0116 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_with_numbers():
    numbers = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9]
    expected_result = {'array': np.array([1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9]),
                       'mode': 5,
                       'entropy': 3.0}
    assert task_func(numbers) == expected_result