import pytest
from collections import Counter
import random
# Constants
HAND_RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'C', 'S']
def task_func():

    hand = []
    for _ in range(5):
        rank = random.choice(HAND_RANKS)
        suit = random.choice(SUITS)
        card = f'{rank}{suit}'
        hand.append(card)

    rank_counts = Counter([card[:-1] for card in hand])

    return hand, rank_counts

def test_task_func():
    hand, rank_counts = task_func()
    assert len(hand) == 5
    assert all(len(card) == 2 for card in hand)
    assert all(rank in HAND_RANKS for rank in hand)
    assert all(suit in SUITS for suit in hand)
    assert isinstance(rank_counts, Counter)
    assert all(rank in rank_counts for rank in HAND_RANKS)
    assert all(rank_counts[rank] >= 1 for rank in HAND_RANKS)
    assert sum(rank_counts.values()) == 5