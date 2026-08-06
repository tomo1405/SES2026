import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def task_func(mu=0, sigma=1):
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, mu, sigma)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    return ax