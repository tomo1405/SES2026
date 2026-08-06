import pytest
from src_0280 import task_func
from collections import Counter

def test_task_func_default():
    result, card_counts = task_func()
    assert len(result) == 1, "Default value of x should be 1"
    assert isinstance(result[0], list), "Each draw should be a list"
    assert len(result[0]) == 5, "Each draw should contain 5 cards"
    assert isinstance(card_counts, Counter), "Return value should be a tuple with a Counter"

def test_task_func_with_x():
    x = 3
    result, card_counts = task_func(x)
    assert len(result) == x, f"Number of draws should be equal to {x}"
    for draw in result:
        assert isinstance(draw, list), "Each draw should be a list"
        assert len(draw) == 5, "Each draw should contain 5 cards"
    assert isinstance(card_counts, Counter), "Return value should be a tuple with a Counter"

def test_task_func_card_counts():
    x = 5
    result, card_counts = task_func(x)
    total_cards_drawn = sum(len(draw) for draw in result)
    assert sum(card_counts.values()) == total_cards_drawn, "Total count of cards in Counter should match total cards drawn"

def test_task_func_card_values():
    x = 2
    result, _ = task_func(x)
    for draw in result:
        for card in draw:
            assert card in CARDS, f"Card {card} is not in the predefined set of cards"