import pytest
from src_0343 import task_func

def test_task_func():
    elements = ['abc', 'def', 'ghi']
    pattern = 'abc'
    seed = 100
    replaced_elements, found = task_func(elements, pattern, seed)
    assert len(replaced_elements) == len(elements)
    for element in replaced_elements:
        assert len(element) == len(element.replace('%', ''))
    assert found