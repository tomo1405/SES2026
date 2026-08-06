python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def task_func(length):
    MU = 0
    SIGMA = 1
    
    distribution = np.random.normal(MU, SIGMA, length)
    fig, ax = plt.subplots()
    ax.hist(distribution, 30, density=True, label='Histogram')
    ax.plot(np.sort(distribution), stats.norm.pdf(np.sort(distribution), MU, SIGMA), 
            linewidth=2, color='r', label='PDF')
    ax.legend()
    
    return distribution, ax