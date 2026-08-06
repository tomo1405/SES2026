python
import random
from collections import Counter
from src_0899 import task_func

def test_task_func():
    random.seed(0)
    pairs = [tuple(random.choices('abcde', k=2)) for _ in range(10)]
    pair_frequency = Counter(pairs)
    assert task_func(10, 0) == pair_frequency