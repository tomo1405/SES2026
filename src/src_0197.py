import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
def task_func(length, range_limit=100, seed=0):
    if range_limit <= 1:
        raise ValueError("range_limit must be greater than 1")

    random.seed(seed)
    np.random.seed(seed)

    random_numbers = [random.randint(1, range_limit) for _ in range(length)]
    random_numbers.sort()

    # Initialize a fresh plot
    plt.figure()
    plot = sns.histplot(random_numbers, kde=False)

    return plot.axes, random_numbers