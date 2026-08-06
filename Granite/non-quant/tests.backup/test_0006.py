import random
import math
from src_0006 import task_func

def test_task_func():
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in task_func.LETTERS}
    sd_dict = task_func(random_dict)
    for k, v in sd_dict.items():
        assert isinstance(k, str) and len(k) == 1, "Key is not a single character string"
        assert all(isinstance(i, int) for i in v), "Values are not all integers"
        assert len(v) >= 1 and len(v) <= 10, "Number of values is not between 1 and 10"
    for k, v in random_dict.items():
        assert k in sd_dict, "Key not found in calculated dictionary"
        assert len(v) == len(sd_dict[k]), "Number of values changed during calculation"