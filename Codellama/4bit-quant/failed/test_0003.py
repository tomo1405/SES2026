import pytest
from src_0003 import task_func

def test_task_func():
    letters = ['A', 'B', 'C']
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in letters}
    sorted_dict = dict(sorted(random_dict.items(), key=lambda item: statistics.mean(item[1]), reverse=True))
    assert task_func(letters) == sorted_dict