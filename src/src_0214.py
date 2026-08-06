import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
def task_func(intervals=100, seed=0):
    random.seed(seed)
    times = []
    numbers = []

    try:
        for _ in range(intervals):
            time.sleep(1)
            times.append(time.time())
            numbers.append(random.random())
    except KeyboardInterrupt:
        print('Interrupted by user')

    kurtosis_value = kurtosis(numbers, nan_policy='omit')
    # Initialize a fresh figure
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(times, numbers)
    return ax, kurtosis_value