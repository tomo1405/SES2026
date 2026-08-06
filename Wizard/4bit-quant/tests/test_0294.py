python
import itertools
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func(elements, subset_size):
    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations]
    ax = plt.hist(sums, bins=np.arange(min(sums), max(sums) + 2) - 0.5, rwidth=0.8, align='left')
    return plt.gca(), combinations, sums

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    expected_ax, expected_combinations, expected_sums = plt.hist([3, 7], bins=np.arange(1, 8) - 0.5, rwidth=0.8, align='left')
    expected_ax.set_title('Histogram of Sums of Combinations of 2 Elements')
    expected_ax.set_xlabel('Sum of Elements')
    expected_ax.set_ylabel('Frequency')
    expected_ax.set_xticks(np.arange(1, 8))
    expected_ax.set_xticklabels([str(i) for i in np.arange(1, 8)])
    expected_ax.set_yticks([0, 1, 2])
    expected_ax.set_yticklabels(['0', '1', '2'])
    expected_ax.grid(axis='y')
    expected_ax.set_ylim(0, 2)
    expected_ax.set_xlim(0.5, 7.5)
    expected_combinations = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    expected_sums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    ax, combinations, sums = task_func(elements, subset_size)
    assert ax.get_title() == expected_ax.get_title()
    assert ax.get_xlabel() == expected_ax.get_xlabel()
    assert ax.get_ylabel() == expected_ax.get_ylabel()
    assert ax.get_xticks().tolist() == expected_ax.get_xticks().tolist()
    assert ax.get_xticklabels().tolist() == expected_ax.get_xticklabels().tolist()
    assert ax.get_yticks().tolist() == expected_ax.get_yticks().tolist()
    assert ax.get_yticklabels().tolist() == expected_ax.get_yticklabels().tolist()
    assert ax.get_ylim() == expected_ax.get_ylim()
    assert ax.get_xlim() == expected_ax.get_xlim()
    assert ax.get_gridlines()[0].get_linestyle() == expected_ax.get_gridlines()[0].get_linestyle()
    assert ax.get_gridlines()[0].get_color() == expected_ax.get_gridlines()[0].get_color()
    assert ax.get_gridlines()[0].get_alpha() == expected_ax.get_gridlines()[0].get_alpha()
    assert ax.get_gridlines()[0].get_linewidth() == expected_ax.get_gridlines()[0].get_linewidth()
    assert combinations == expected_combinations
    assert sums == expected_sums