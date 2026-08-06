import pytest
from src_0280 import task_func

def test_task_func():
    result, card_counts = task_func()
    assert len(result) == 5
    assert all(isinstance(card, str) for card in result)
    assert all(card in CARDS for card in result)
    assert all(card_counts[card] == 1 for card in result)