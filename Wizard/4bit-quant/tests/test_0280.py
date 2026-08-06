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
    assert len(result[0]) == 5
    assert all(card in CARDS for card in result[0])
    assert all(count == 1 for count in card_counts.values())

    # Test custom value of x
    result, card_counts = task_func(x=3)
    assert len(result) == 3
    assert all(len(drawn) == 5 for drawn in result)
    assert all(all(card in CARDS for card in drawn) for drawn in result)
    assert all(all(count == 1 for count in card_counts.values()) for drawn in result)