import pytest
from src_0817 import task_func
from collections import Counter

def test_task_func():
    hand, rank_counts = task_func()

    # Check that hand is a list of 5 cards
    assert isinstance(hand, list)
    assert len(hand) == 5

    # Check that each card is a string of length 2
    for card in hand:
        assert isinstance(card, str)
        assert len(card) == 2

    # Check that each card's rank is in HAND_RANKS and suit is in SUITS
    for card in hand:
        rank, suit = card[:-1], card[-1]
        assert rank in HAND_RANKS
        assert suit in SUITS

    # Check that rank_counts is a Counter object
    assert isinstance(rank_counts, Counter)

    # Check that the sum of rank_counts values is 5
    assert sum(rank_counts.values()) == 5

    # Check that each rank count is between 0 and 5
    for count in rank_counts.values():
        assert 0 <= count <= 5