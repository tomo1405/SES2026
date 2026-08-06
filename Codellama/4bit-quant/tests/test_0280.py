import pytest
from src_0280 import task_func

def test_task_func():
    result, card_counts = task_func()
    assert len(result) == 5
    assert all(len(x) == 5 for x in result)
    assert all(x in CARDS for x in result)
    assert card_counts.most_common() == [('2', 1), ('3', 1), ('4', 1), ('5', 1), ('6', 1), ('7', 1), ('8', 1), ('9', 1), ('10', 1), ('J', 1), ('Q', 1), ('K', 1), ('A', 1)]