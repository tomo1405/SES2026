python
import itertools
import numpy as np
import matplotlib.pyplot as plt

def task_func(elements, subset_size):
    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations]
    ax = plt.hist(sums, bins=np.arange(min(sums), max(sums) + 2) - 0.5, rwidth=0.8, align='left')
    return plt.gca(), combinations, sums

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    expected_ax, expected_combinations, expected_sums = plt.hist([3, 7, 10], bins=np.arange(min([3, 7, 10]), max([3, 7, 10]) + 2) - 0.5, rwidth=0.8, align='left')
    expected_ax.set_title('Histogram of Sums of Subsets of Size 2')
    expected_ax.set_xlabel('Sum of Subset')
    expected_ax.set_ylabel('Frequency')
    expected_ax.set_xticks(np.arange(min([3, 7, 10]), max([3, 7, 10]) + 1))
    expected_ax.set_xticklabels(['3', '4', '5', '6', '7', '8', '9', '10'])
    expected_ax.set_yticks([0, 1, 2, 3])
    expected_ax.set_yticklabels(['0', '1', '2', '3'])
    expected_ax.set_ylim(0, 3)
    expected_ax.set_xlim(2.5, 9.5)
    expected_combinations = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    expected_sums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ax, combinations, sums = task_func(elements, subset_size)
    assert ax.get_title() == expected_ax.get_title()
    assert ax.get_xlabel() == expected_ax.get_xlabel()
    assert ax.get_ylabel() == expected_ax.get_ylabel()
    assert ax.get_xticks().tolist() == expected_ax.get_xticks().tolist()
    assert ax.get_xticklabels() == expected_ax.get_xticklabels()
    assert ax.get_yticks().tolist() == expected_ax.get_yticks().tolist()
    assert ax.get_yticklabels() == expected_ax.get_yticklabels()
    assert ax.get_ylim() == expected_ax.get_ylim()
    assert ax.get_xlim() == expected_ax.get_xlim()
    assert combinations == expected_combinations
    assert sums == expected_sums

test_task_func()