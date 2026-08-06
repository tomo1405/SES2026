import re
import random
import string
import pytest

def task_func(n, pattern, seed=None):
    if seed is not None:
        random.seed(seed)
    rand_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    matches = re.findall(pattern, rand_str)
    return matches

def test_task_func():
    n = 10
    pattern = r'\d'
    seed = 42
    matches = task_func(n, pattern, seed)
    assert len(matches) == 2
    assert matches[0] != matches[1]

if __name__ == "__main__":
    pytest.main()