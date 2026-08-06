import pytest
from src_0280 import task_func

def test_task_func():
    result, card_counts = task_func(x=3)
    assert len(result) == 3
    assert len(card_counts) > 0
    assert all(isinstance(card, str) for card in card_counts)