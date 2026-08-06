import pytest
from src_0530 import task_func

def test_task_func():
    num_rolls = 1000
    num_dice = 2
    plot_path = None
    random_seed = 0

    sums_counter, ax = task_func(num_rolls, num_dice, plot_path, random_seed)

    assert isinstance(sums_counter, Counter)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(sums_counter) == num_rolls
    assert all(sum(roll) in sums_counter for roll in sums_counter.keys())
    assert all(sums_counter[sum(roll)] == 1 for roll in sums_counter.keys())
    assert ax.get_xlabel() == "Sum of Dice Roll"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Distribution of Dice Roll Sums"
    assert ax.get_xlim() == (1, 12)
    assert ax.get_ylim() == (0, num_rolls)
    assert ax.get_xticks() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert ax.get_yticks() == [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    assert ax.get_xticklabels() == [str(i) for i in range(1, 13)]
    assert ax.get_yticklabels() == [str(i) for i in range(0, 1001, 100)]