from collections import Counter

from src_0817 import task_func


def test_task_func():
    hand, rank_counts = task_func()
    
    # Check that the hand has 5 cards
    assert len(hand) == 5
    
    # Check that each card is in the correct format
    for card in hand:
        assert len(card) == 2
        assert card[0] in HAND_RANKS
        assert card[1] in SUITS
    
    # Check that rank_counts is a Counter object
    assert isinstance(rank_counts, Counter)
    
    # Check that the sum of rank_counts values is 5
    assert sum(rank_counts.values()) == 5