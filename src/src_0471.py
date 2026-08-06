import matplotlib.pyplot as plt
import numpy as np
def task_func(myList):
    _, ax = plt.subplots()
    ax.hist(
        myList, bins=np.arange(min(myList), max(myList) + 2) - 0.5, edgecolor="black"
    )
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Values")
    return ax