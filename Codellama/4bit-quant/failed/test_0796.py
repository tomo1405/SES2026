import pytest
from src_0796 import task_func

def test_task_func_empty_list():
    assert task_func([]) == deque()

def test_task_func_non_empty_list():
    assert task_func([1, 2, 3]) == deque([1, 2, 3])

def test_task_func_numeric_sum():
    assert task_func([1, 2, 3]) == deque([1, 2, 3])
    assert math.sqrt(sum(item for item in dq if isinstance(item, (int, float)))) == 3

def test_task_func_print_statement():
    with pytest.raises(SystemExit):
        task_func([1, 2, 3])