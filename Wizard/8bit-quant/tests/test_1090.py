python
import pytest
from src_1090 import task_func

def test_task_func():
    list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c')]
    total_sum, category_counts = task_func(list_of_tuples)
    assert total_sum == 10
    assert category_counts == {'a': 2, 'b': 1, 'c': 1}