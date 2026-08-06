from typing import Counter

from src_0817 import task_func


def test_task_func():
    hand, rank_counts = task_func()

    # Check that hand is a list of 5 elements
    assert isinstance(hand, list)
    assert len(hand) == 5

    # Check that each element in hand is a string of length 2
    for card in hand:
        assert isinstance(card, str)
        assert len(card) == 2

    # Check that each rank in hand is valid
    for card in hand:
        rank = card[0]
        assert rank in HAND_RANKS

    # Check that each suit in hand is valid
    for card in hand:
        suit = card[1]
        assert suit in SUITS

    # Check that rank_counts is a Counter object
    assert isinstance(rank_counts, Counter)

    # Check that the sum of rank_counts values is 5
    assert sum(rank_counts.values()) == 5

    # Check that each key in rank_counts is a valid rank
    for rank in rank_counts.keys():
        assert rank in HAND_RANKS