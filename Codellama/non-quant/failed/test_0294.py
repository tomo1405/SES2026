import pytest
from src_0294 import task_func

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    ax, combinations, sums = task_func(elements, subset_size)
    assert ax is not None
    assert len(combinations) == 10
    assert len(sums) == 10
    assert all(sum(combination) == 6 for combination in combinations)
    assert all(sum(combination) in sums for combination in combinations)
    assert all(ax.get_xlim() == (1, 6))
    assert all(ax.get_ylim() == (0, 10))
    assert all(ax.get_title() == 'Histogram of Subset Sums')
    assert all(ax.get_xlabel() == 'Subset Sum')
    assert all(ax.get_ylabel() == 'Frequency')
    assert all(ax.get_xticks() == np.arange(1, 7))
    assert all(ax.get_yticks() == np.arange(0, 11))