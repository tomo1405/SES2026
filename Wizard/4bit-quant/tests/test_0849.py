python
import heapq
import random
import pytest

from src_0849 import task_func

@pytest.mark.parametrize("obj_list, attr, top_n, seed, expected", [
    ([], "age", 5, None, ([], None)),
    ([{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}], "age", 2, None, ([35, 30], 30)),
    ([{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}], "age", 3, 42, ([35, 30, 25], 30)),
    ([{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}], "name", 2, None, ([], None)),
    ([{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}], "name", 3, 42, ([], None)),
])
def test_task_func(obj_list, attr, top_n, seed, expected):
    result = task_func(obj_list, attr, top_n, seed)
    assert result == expected