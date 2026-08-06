import json
import random

from src_0126 import task_func


def test_task_func():
    LETTERS = ['A', 'B', 'C', 'D', 'E']
    n = 3
    filename = task_func(LETTERS, n)
    assert filename == f'letter_combinations_{random.randint(1, 100)}.json'
    with open(filename, 'r') as f:
        letter_counts = json.load(f)
    assert letter_counts == {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1}