import random
import math
from src_0006 import task_func

def test_task_func():
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in task_func.LETTERS}
    sd_dict = task_func(random_dict)
    for k, v in sd_dict.items():
        assert isinstance(k, str)
        assert isinstance(v, float)
        assert len(k) == 1
        assert v >= 0