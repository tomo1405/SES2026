import pytest
from src_0817 import task_func

def test_task_func():
    hand, rank_counts = task_func()
    assert len(hand) == 5
    assert len(rank_counts) == 10
    for card in hand:
        assert card[:-1] in HAND_RANKS
        assert card[-1] in SUITS
    for rank, count in rank_counts.items():
        assert rank in HAND_RANKS
        assert count == 1