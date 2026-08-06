import pytest
from src_0861 import task_func
import re
import random
import string

def test_task_func():
    n = 10  # Example input for n
    pattern = r'[a-z]+'  # Example input for pattern
    seed = 42  # Example input for seed
    random.seed(seed)
    rand_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    expected_matches = re.findall(pattern, rand_str)
    actual_matches = task_func(n, pattern, seed)
    assert actual_matches == expected_matches