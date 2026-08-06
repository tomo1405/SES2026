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
import pytest

def test_task_func():
    x = [np.linspace(-5, 5, 100) for _ in range(3)]
    y = [np.random.normal(loc=i, scale=1, size=100) for i in range(3)]
    labels = [f"Label {i+1}" for i in range(3)]
    
    fig = task_func(x, y, labels)
    
    assert fig is not None
    assert isinstance(fig, plt.Figure)