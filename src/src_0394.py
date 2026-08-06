import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(mu, sigma, num_samples=1000, seed=77):
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)

    fig = plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    plt.subplot(1, 2, 2)
    stats.probplot(samples, dist="norm", plot=plt)

    return fig