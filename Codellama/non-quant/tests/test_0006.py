import math
import random

from src_0006 import task_func


def test_task_func():
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    sd_dict = {
        k: math.sqrt(sum((i - sum(v) / len(v)) ** 2 for i in v) / len(v))
        for k, v in random_dict.items()
    }
    assert sd_dict == task_func()