import pytest
from src_0116 import task_func

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_valid_input():
    numbers = [1, 2, 3, 4, 5]
    expected_output = {'array': np.array(numbers), 'mode': 3, 'entropy': 1.3862943611198906}
    assert task_func(numbers) == expected_output

def test_task_func_invalid_input():
    numbers = [1, 2, 3, 4, 5, 6]
    with pytest.raises(ValueError):
        task_func(numbers)