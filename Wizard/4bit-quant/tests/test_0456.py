python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pytest

def task_func(mean, std_dev, n):
    samples = np.random.normal(mean, std_dev, n)

    plt.figure(figsize=(10, 6))
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std_dev)
    plt.plot(x, p, 'k', linewidth=2)

    title = f'Normal Distribution: Mean = {mean}, Std Dev = {std_dev}'
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.show()

    return samples

def test_task_func():
    # Test case 1
    mean = 50
    std_dev = 10
    n = 1000
    samples = task_func(mean, std_dev, n)
    assert len(samples) == n
    assert np.mean(samples) == pytest.approx(mean, abs=0.1)
    assert np.std(samples) == pytest.approx(std_dev, abs=0.1)

    # Test case 2
    mean = 100
    std_dev = 20
    n = 500
    samples = task_func(mean, std_dev, n)
    assert len(samples) == n
    assert np.mean(samples) == pytest.approx(mean, abs=0.1)
    assert np.std(samples) == pytest.approx(std_dev, abs=0.1)