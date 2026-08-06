import pytest
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
from matplotlib.axes import Axes

class ValueObject:
    value = 0
    def __init__(self, mu=0, std=1, seed=77):
        random.seed(seed)
        self.value = random.gauss(mu, std)

def task_func(obj_list) -> Axes:
    if len(obj_list) == 0:
        values = [0]
    else:
        values = [obj.value for obj in obj_list]

    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Plot histogram
    ax.hist(values, bins=30, density=True, alpha=0.6, color='g')
    mean = np.mean(values)
    std = np.std(values)

    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std)
    ax.plot(x, p, 'k', linewidth=2)

    title = "Fit results: mu = %.2f,  std = %.2f" % (mean, std)
    ax.set_title(title)

    plt.close(fig)  # Close the figure to avoid display during function execution
    return ax

@pytest.mark.parametrize("obj_list, expected_mean, expected_std", [
    ([ Vo(mu=10, std=2, seed=123) for _ in range(100) ], 10, 2),
    ([ Vo(mu=5, std=1, seed=456) for _ in range(100) ], 5, 1),
    ([], 0, 0),
])
def test_task_func(obj_list, expected_mean, expected_std):
    ax = task_func(obj_list)
    values = [obj.value for obj in obj_list]
    assert np.isclose(np.mean(values), expected_mean, rtol=0.1)
    assert np.isclose(np.std(values), expected_std, rtol=0.1)
    assert ax.get_title() == f"Fit results: mu = {expected_mean:.2f},  std = {expected_std:.2f}"