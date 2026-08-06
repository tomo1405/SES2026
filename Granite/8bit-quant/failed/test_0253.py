import matplotlib.pyplot as plt
from itertools import zip_longest
# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']
def task_func(data, labels):
    fig, ax = plt.subplots()
    for series, label, color in zip_longest(data, labels, COLORS, fillvalue='black'):
        ax.plot(series, label=label, color=color)
        
    ax.legend()
    return ax