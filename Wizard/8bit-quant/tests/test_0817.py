python
import random
from collections import Counter

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
    assert len(rank_counts) == 13
    for rank in HAND_RANKS:
        assert rank_counts[rank] == 1