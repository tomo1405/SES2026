python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    sample = np.random.normal(mean, std_dev, 1000)
    plot_paths = []

    # Plotting histogram
    plt.figure()
    plt.hist(sample, bins=50)
    if save_plots:
        hist_path = "histogram_plot.png"
        plt.savefig(hist_path)
        plt.close()
        plot_paths.append(hist_path)

    # Plotting QQ diagram
    plt.figure()
    stats.probplot(sample, plot=plt)
    if save_plots:
        qq_path = "qq_plot.png"
        plt.savefig(qq_path)
        plt.close()
        plot_paths.append(qq_path)

    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)

    return skewness, kurtosis, plot_paths