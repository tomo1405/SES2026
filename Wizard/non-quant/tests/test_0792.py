python
import pytest
from src_0792 import task_func

def test_task_func():
    # Test case 1
    assert task_func([]) == Counter()

    # Test case 2
    l = [1, 2, 3, 4, 5]
    random.shuffle(l)
    l_cycled = cycle(l)
    counter = Counter(next(l_cycled) for _ in range(30))
    keys = list(counter.keys())
    counter = Counter({k: counter[k] for k in keys[3:] + keys[:3]})
    assert task_func(l) == counter

    # Test case 3
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(l)
    l_cycled = cycle(l)
    counter = Counter(next(l_cycled) for _ in range(30))
    keys = list(counter.keys())
    counter = Counter({k: counter[k] for k in keys[3:] + keys[:3]})
    assert task_func(l) == counter

    # Test case 4
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    random.shuffle(l)
    l_cycled = cycle(l)
    counter = Counter(next(l_cycled) for _ in range(30))
    keys = list(counter.keys())
    counter = Counter({k: counter[k] for k in keys[3:] + keys[:3]})
    assert task_func(l) == counter