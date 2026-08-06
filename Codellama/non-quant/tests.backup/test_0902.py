import pytest
from src_0902 import task_func

def test_task_func_empty_input():
    d = []
    expected_output = pd.DataFrame(columns=['x', 'y', 'z'])
    assert task_func(d).equals(expected_output)

def test_task_func_non_empty_input():
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    expected_output = pd.DataFrame(data=[(0.5, 0.5, 0.5), (1, 1, 1)], columns=['x', 'y', 'z'])
    assert task_func(d).equals(expected_output)