import itertools
import numpy as np
import matplotlib.pyplot as plt
def task_func(elements, subset_size):
    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations]
    ax = plt.hist(sums, bins=np.arange(min(sums), max(sums) + 2) - 0.5, rwidth=0.8, align='left')
    return plt.gca(), combinations, sums