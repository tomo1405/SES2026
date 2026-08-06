import itertools
import random
def task_func(t, n):
    combinations = list(itertools.combinations(t, n))
    selected_combination = random.choice(combinations)

    return selected_combination