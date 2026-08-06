python
import itertools
import random
import pytest

from src_0001 import task_func

@pytest.mark.parametrize("numbers", [list(range(1, 3)), [1, 2, 3], [4, 5, 6]])
def test_task_func(numbers):
    permutations = list(itertools.permutations(numbers))
    sum_diffs = 0

    for perm in permutations:
        perm = list(perm)
        random.shuffle(perm)
        diffs = [abs(perm[i] - perm[i+1]) for i in range(len(perm)-1)]
        sum_diffs += sum(diffs)

    avg_sum_diffs = sum_diffs / len(permutations)
    
    assert task_func(numbers) == avg_sum_diffs