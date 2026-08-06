import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
def task_func(x, y, labels):
    fig, ax = plt.subplots()

    for i in range(len(x)):
        mu = np.mean(y[i])
        sigma = np.std(y[i])
        pdf = stats.norm.pdf(x[i], mu, sigma)
        ax.plot(x[i], pdf, label=labels[i])
    
    ax.legend()
    
    return fig