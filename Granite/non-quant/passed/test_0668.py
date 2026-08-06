import pytest
from src_0668 import task_func

def test_task_func():
    assert task_func([1, 2, 3, 2, 2, 1, 4, 5, 4, 3], 3) == [1, 2, 3]
    assert task_func([1, 2, 3, 4, 5], 2) == [1, 2]
    assert task_func([1, 1, 1, 1, 1], 1) == [1]
    assert task_func([5, 4, 3, 2, 1], 3) == [5, 4, 3]
    assert task_func([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

if __name__ == "__main__":
    pytest.main()