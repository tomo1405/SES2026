import itertools
import statistics
# Refined function after importing required libraries
def task_func(elements, subset_size):
    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations]
    return {
        'mean': statistics.mean(sums),
        'median': statistics.median(sums),
        'mode': statistics.mode(sums)
    }