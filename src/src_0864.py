import numpy as np
import math
# Constants
POSSIBLE_NUMBERS = np.arange(1, 11)
def task_func(list_of_lists):
    sums = []
    for list_ in list_of_lists:
        sum_ = sum(math.pow(x, 2) for x in POSSIBLE_NUMBERS[:len(list_)])
        sums.append(sum_)

    return sums