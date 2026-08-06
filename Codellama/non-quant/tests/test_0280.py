import pytest
from src_0280 import task_func


def test_task_func():
    result, card_counts = task_func()
    assert len(result) == 5
    assert all(len(hand) == 5 for hand in result)
    assert all(card in CARDS for hand in result for card in hand)
    assert all(card_counts[card] == 1 for card in CARDS)

def test_task_func_with_x():
    result, card_counts = task_func(x=10)
    assert len(result) == 10
    assert all(len(hand) == 5 for hand in result)
    assert all(card in CARDS for hand in result for card in hand)
    assert all(card_counts[card] == 1 for card in CARDS)

def test_task_func_with_invalid_x():
    with pytest.raises(ValueError):
        task_func(x=-1)
    with pytest.raises(ValueError):
        task_func(x=0)
    with pytest.raises(ValueError):
        task_func(x=1.5)
    with pytest.raises(ValueError):
        task_func(x='hello')