import pytest
from src_0004 import task_func

def test_task_func():
    LETTERS = ['A', 'B', 'C']
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    mean_dict = {k: np.mean(v) for k, v in random_dict.items()}
    assert task_func(LETTERS) == mean_dict