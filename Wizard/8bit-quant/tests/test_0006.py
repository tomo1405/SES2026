python
import random
import math

def task_func(LETTERS=[chr(i) for i in range(97, 123)]):
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    sd_dict = {
        k: math.sqrt(sum((i - sum(v) / len(v)) ** 2 for i in v) / len(v))
        for k, v in random_dict.items()
    }
    return sd_dict

def test_task_func():
    assert task_func() == {'a': 10.0, 'b': 10.0, 'c': 10.0, 'd': 10.0, 'e': 10.0, 'f': 10.0, 'g': 10.0, 'h': 10.0, 'i': 10.0, 'j': 10.0, 'k': 10.0, 'l': 10.0, 'm': 10.0, 'n': 10.0, 'o': 10.0, 'p': 10.0, 'q': 10.0, 'r': 10.0, 's': 10.0, 't': 10.0, 'u': 10.0, 'v': 10.0, 'w': 10.0, 'x': 10.0, 'y': 10.0, 'z': 10.0}

test_task_func()