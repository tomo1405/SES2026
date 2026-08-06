import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
# Constants
RANGE = 10000  # The range within which random numbers are generated
SIZE = 1000  # The number of random numbers to generate
BIN_WIDTH = 100  # The width of bins for the histogram
def task_func():
    numbers = [random.randint(0, RANGE) for _ in range(SIZE)]
    moving_avg = [statistics.mean(numbers[max(0, i - 5):i + 1]) for i in range(SIZE)]

    df = pd.DataFrame({
        'Random Numbers': numbers,
        'Moving Average': moving_avg
    })

    plt.hist(df['Random Numbers'],
             bins=np.arange(min(df['Random Numbers']), max(df['Random Numbers']) + BIN_WIDTH, BIN_WIDTH))
    plt.title('Histogram of Random Numbers')
    plt.xlabel('Random Numbers')
    plt.ylabel('Frequency')
    plt.show()

    return df