import pytest
from collections import Counter
import random

from src_0817 import task_func

HAND_RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'C', 'S']

def test_task_func():
    hand, rank_counts = task_func()
    assert len(hand) == 5
    for card in hand:
        assert card[0] in HAND_RANKS
        assert card[1] in SUITS
    assert isinstance(rank_counts, Counter)
    for rank in HAND_RANKS:
        assert rank_counts[rank] >= 0

def test_task_func_with_seed():
    random.seed(42)
    hand1, rank_counts1 = task_func()
    random.seed(42)
    hand2, rank_counts2 = task_func()
    assert hand1 == hand2
    assert rank_counts1 == rank_counts2