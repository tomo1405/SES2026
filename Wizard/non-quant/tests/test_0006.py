python
import random
import math
import pytest

from src_0006 import task_func

LETTERS = [chr(i) for i in range(97, 123)]

@pytest.fixture
def random_dict():
    return {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}

def test_task_func(random_dict):
    sd_dict = {
        k: math.sqrt(sum((i - sum(v) / len(v)) ** 2 for i in v) / len(v))
        for k, v in random_dict.items()
    }
    assert task_func(LETTERS) == sd_dict