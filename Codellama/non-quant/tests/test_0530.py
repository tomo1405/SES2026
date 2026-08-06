from typing import Counter

import matplotlib
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
    assert all(label in POSSIBLE_VALUES for label in sums_counter.keys())
    assert all(value in range(1, 7) for value in sums_counter.values())
    assert all(label in ax.get_xticks() for label in sums_counter.keys())
    assert all(value in ax.get_yticks() for value in sums_counter.values())
    assert ax.get_xlabel() == "Sum of Dice Roll"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Distribution of Dice Roll Sums"