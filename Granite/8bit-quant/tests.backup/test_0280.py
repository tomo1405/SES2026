import pytest
from src_0280 import task_func
from collections import Counter
import random

# Constants
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def test_task_func():
    result, card_counts = task_func()
    assert isinstance(result, list)
    assert all(isinstance(item, list) for item in result)
    assert all(len(item) == 5 for item in result)
    assert all(item in CARDS for item in sum(result, []))
    assert isinstance(card_counts, Counter)
    assert card_counts.most_common(1)[0][1] == 1

def test_task_func_with_x():
    x = random.randint(2, 10)
    result, card_counts = task_func(x)
    assert isinstance(result, list)
    assert all(isinstance(item, list) for item in result)
    assert all(len(item) == 5 for item in result)
    assert all(item in CARDS for item in sum(result, []))
    assert isinstance(card_counts, Counter)
    assert sum(card_counts.values()) == x