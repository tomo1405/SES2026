import pytest
from src_0817 import task_func

def test_task_func():
    hand, rank_counts = task_func()
    assert len(hand) == 5
    assert len(rank_counts) == 10
    assert all(rank in HAND_RANKS for rank in rank_counts.keys())
    assert all(suit in SUITS for suit in hand)