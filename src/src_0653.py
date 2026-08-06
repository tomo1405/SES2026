import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
# Constants
TARGET_VALUE = '332'
ARRAY = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
def task_func(target_value=TARGET_VALUE, array=ARRAY):
    indices = np.where(array[:, 0] == target_value)[0]

    # Check if statistical analysis is possible
    if len(indices) < 2:
        # Not enough data for meaningful statistical analysis
        plt.hist(indices, bins='auto')  # Plotting can still occur
        plt.show()
        return (np.mean(indices), 'N/A', 'N/A', 'N/A') if indices.size else ('N/A', 'N/A', 'N/A', 'N/A')

    # Perform statistical analysis
    mean = np.mean(indices)
    variance = np.var(indices)
    skewness = stats.skew(indices)
    kurtosis = stats.kurtosis(indices)

    # Plot the distribution
    plt.hist(indices, bins='auto')
    plt.title('Distribution of Indices')
    plt.xlabel('Indices')
    plt.ylabel('Frequency')
    plt.show()

    return mean, variance, skewness, kurtosis