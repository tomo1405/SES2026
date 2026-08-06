python
import pytest
from src_0547 import task_func

def test_task_func():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    expected_table = PrettyTable(['Key', 'Value'])
    expected_table.add_row(['a', 1])
    expected_table.add_row(['b', 2])
    expected_table.add_row(['c', 3])

    assert task_func(my_dict) == expected_table