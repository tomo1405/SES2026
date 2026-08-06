python
import random
from collections import Counter
import pytest

# Constants
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def task_func(x=1):
    result = []
    card_counts = Counter()

    for i in range(x):
        drawn = random.sample(CARDS, 5)
        result.append(drawn)
        card_counts.update(drawn)

    return result, card_counts

def test_task_func():
    # Test default value of x
    result, card_counts = task_func()
    assert len(result) == 1
    assert len(card_counts) == 5
    assert all(card in card_counts for card in CARDS)

    # Test x=2
    result, card_counts = task_func(2)
    assert len(result) == 2
    assert len(card_counts) == 10
    assert all(card in card_counts for card in CARDS)

    # Test x=0
    result, card_counts = task_func(0)
    assert len(result) == 0
    assert len(card_counts) == 0