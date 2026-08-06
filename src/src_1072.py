import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle
COLORS = ["b", "g", "r", "c", "m", "y", "k"]
def task_func(list_of_lists):
    fig, ax = plt.subplots()
    color_cycle = cycle(COLORS)

    for list_ in list_of_lists:
        y_values = np.arange(1, len(list_) + 1)
        shuffle(y_values)
        ax.plot(y_values, next(color_cycle))

    return fig, ax