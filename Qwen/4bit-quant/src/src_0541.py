from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    # Flatten the list
    flat_list = list(itertools.chain(*list_of_menuitems))

    # Count the occurrences of each menu item
    counter = Counter(flat_list)
    labels, values = zip(*sorted(counter.items(), key=lambda x: x[0]))
    indexes = np.arange(len(labels))

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(indexes, values, width, color=color)
    ax.set_xticklabels(labels)
    ax.set_xlabel("Menu Items")
    ax.set_ylabel("Frequency")
    ax.set_title(title)

    return ax