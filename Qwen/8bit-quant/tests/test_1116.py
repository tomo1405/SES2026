import random
from string import ascii_uppercase

from src_1116 import task_func


def test_task_func_with_empty_dict():
    assert task_func({}) == []

def test_task_func_with_single_prefix():
    result = task_func({'A': 2})
    assert len(result) == 2
    for emp_id in result:
        assert emp_id.startswith('A')
        assert len(emp_id) == 6
        assert emp_id[1:] in set(''.join(random.choices(ascii_uppercase, k=5)) for _ in range(100))

def test_task_func_with_multiple_prefixes():
    result = task_func({'A': 1, 'B': 2})
    assert len(result) == 3
    for emp_id in result:
        if emp_id.startswith('A'):
            assert len(emp_id) == 6
            assert emp_id[1:] in set(''.join(random.choices(ascii_uppercase, k=5)) for _ in range(100))
        elif emp_id.startswith('B'):
            assert len(emp_id) == 6
            assert emp_id[1:] in set(''.join(random.choices(ascii_uppercase, k=5)) for _ in range(100))

def test_task_func_with_zero_employees():
    result = task_func({'A': 0, 'B': 2})
    assert len(result) == 2
    for emp_id in result:
        assert emp_id.startswith('B')
        assert len(emp_id) == 6
        assert emp_id[1:] in set(''.join(random.choices(ascii_uppercase, k=5)) for _ in range(100))

def test_task_func_with_large_number_of_employees():
    result = task_func({'A': 10})
    assert len(result) == 10
    for emp_id in result:
        assert emp_id.startswith('A')
        assert len(emp_id) == 6
        assert emp_id[1:] in set(''.join(random.choices(ascii_uppercase, k=5)) for _ in range(100))