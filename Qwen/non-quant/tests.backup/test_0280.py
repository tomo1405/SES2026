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

def test_task_func_multiple_draws():
    x = 3
    result, card_counts = task_func(x)
    assert len(result) == x
    for draw in result:
        assert isinstance(draw, list)
        assert len(draw) == 5
        assert all(card in CARDS for card in draw)
    assert isinstance(card_counts, Counter)
    assert sum(card_counts.values()) == 5 * x

def test_task_func_no_draws():
    result, card_counts = task_func(0)
    assert len(result) == 0
    assert isinstance(card_counts, Counter)
    assert sum(card_counts.values()) == 0

def test_task_func_large_number_of_draws():
    x = 100
    result, card_counts = task_func(x)
    assert len(result) == x
    for draw in result:
        assert isinstance(draw, list)
        assert len(draw) == 5
        assert all(card in CARDS for card in draw)
    assert isinstance(card_counts, Counter)
    assert sum(card_counts.values()) == 5 * x

def test_task_func_card_counts():
    x = 2
    result, card_counts = task_func(x)
    for card in CARDS:
        count = sum(draw.count(card) for draw in result)
        assert card_counts[card] == count