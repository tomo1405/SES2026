import pytest
from src_0817 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, tuple), "The function should return a tuple."
    hand, rank_counts = result
    assert isinstance(hand, list), "The hand should be a list."
    assert isinstance(rank_counts, Counter), "The rank_counts should be a Counter instance."
    assert len(hand) == 5, "The hand should contain 5 cards."
    assert all(card.isdigit() or card[0] in 'JQKA' for card in hand), "Each card should be in the correct format."
    assert all(rank in rank_counts for rank in HAND_RANKS), "All ranks in the hand should be valid."