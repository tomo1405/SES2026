import pytest
from src_0198 import task_func

def test_task_func():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 4, 6, 8, 10]
    N = 3

    ax = task_func(l1, l2, N)

    assert len(ax.get_lines()) == N
    assert all(abs(l1[i] - l2[i]) == ax.get_lines()[i].get_ydata() for i in range(N))