import pytest
from src_0294 import task_func

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    ax, combinations, sums = task_func(elements, subset_size)
    assert ax is not None
    assert len(combinations) == 10
    assert len(sums) == 10
    assert all(sum(combination) == sum for combination in combinations)
    assert all(sum in sums for sum in sums)
    assert all(sum in np.arange(min(sums), max(sums) + 2) - 0.5 for sum in sums)
    assert all(ax.get_xlim() == (min(sums), max(sums) + 2) - 0.5)
    assert all(ax.get_ylim() == (0, 10))
    assert all(ax.get_title() == 'Histogram of Sum of Subsets')
    assert all(ax.get_xlabel() == 'Sum of Subsets')
    assert all(ax.get_ylabel() == 'Frequency')