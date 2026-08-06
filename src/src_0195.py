import numpy as np
import matplotlib.pyplot as plt
# Constants
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
def task_func(data_size):
    np.random.seed(0)
    data = np.random.randn(data_size)
    color = np.random.choice(BAR_COLOR)
    plt.hist(data, bins=np.arange(-3, 4, 0.5), color=color, edgecolor='black')
    return data, color