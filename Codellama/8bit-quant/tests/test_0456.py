import numpy as np
from src_0456 import task_func


def test_task_func():
    mean = 0
    std_dev = 1
    n = 100
    samples = task_func(mean, std_dev, n)

    assert len(samples) == n
    assert np.all(samples >= 0)
    assert np.all(samples <= 1)

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