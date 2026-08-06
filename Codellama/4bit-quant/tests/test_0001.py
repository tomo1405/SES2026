import itertools

from src_0001 import task_func


def test_task_func():
    numbers = [1, 2, 3]
    permutations = list(itertools.permutations(numbers))
    expected_avg_sum_diffs = 0

    for perm in permutations:
        perm = list(perm)
        shuffle(perm)
        diffs = [abs(perm[i] - perm[i+1]) for i in range(len(perm)-1)]
        expected_avg_sum_diffs += sum(diffs)

    expected_avg_sum_diffs /= len(permutations)

    assert task_func(numbers) == expected_avg_sum_diffs