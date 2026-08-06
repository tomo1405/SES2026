import matplotlib.pyplot as plt
import random
# Constants
COLORS = ['#00bfbf', '#000000', '#0000ff']
def task_func(number_list, bins):

    fig, ax = plt.subplots()
    color = random.choice(COLORS)  # Randomly select color from the COLORS constant
    ax.hist(number_list, bins=bins, color=color)
    ax.set_title('Histogram')
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')
    return ax