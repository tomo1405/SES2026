import pytest
from src_0280 import task_func
from collections import Counter

def test_task_func_default():
    result, card_counts = task_func()
    assert len(result) == 1
    assert isinstance(result[0], list)
    assert len(result[0]) == 5
    assert all(card in CARDS for card in result[0])
    assert isinstance(card_counts, Counter)
    assert sum(card_counts.values()) == 5

def test_task_func_custom_draws():
    x = 3
    result, card_counts = task_func(x)
    assert len(result) == x
    for draw in result:
        assert isinstance(draw, list)
        assert len(draw) == 5
        assert all(card in CARDS for card in draw)
    assert isinstance(card_counts, Counter)
    assert sum(card_counts.values()) == x * 5

def test_task_func_no_duplicates_within_draw():
    result, _ = task_func()
    assert len(set(result[0])) == 5

def test_task_func_card_counts():
    x = 2
    result, card_counts = task_func(x)
    for card in CARDS:
        assert card_counts[card] <= x

def test_task_func_randomness():
    _, card_counts1 = task_func(10)
    _, card_counts2 = task_func(10)
    assert card_counts1 != card_counts2