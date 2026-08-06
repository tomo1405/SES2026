python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    if n_samples <= 0 or sigma <= 0:
        raise ValueError("Invalid n_samples or sigma")
    np.random.seed(random_seed)
    plt.figure()
    samples = np.random.normal(mu, sigma, n_samples)
    _, _, _ = plt.hist(samples, 30, density=True)
    ax = plt.gca()
    ax.plot(
        np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000),
        norm.pdf(np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000), mu, sigma),
        linewidth=2,
        color="r",
    )
    return ax, samples

def test_task_func():
    ax, samples = task_func(n_samples=1000, mu=0, sigma=1, random_seed=0)
    assert ax is not None
    assert samples is not None
    assert len(samples) == 1000
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'Probability density'
    assert ax.get_title() == 'Histogram of samples'
    assert ax.get_xlim() == (-4.0, 4.0)
    assert ax.get_ylim() == (0.0, 0.4)
    assert ax.get_xticks() == [-4, -2, 0, 2, 4]
    assert ax.get_yticks() == [0, 0.1, 0.2, 0.3, 0.4]
    assert ax.get_legend().get_texts()[0].get_text() == 'Histogram'
    assert ax.get_legend().get_texts()[1].get_text() == 'Normal distribution'
    assert ax.get_legend().get_lines()[0].get_color() == 'blue'
    assert ax.get_legend().get_lines()[1].get_color() == 'red'
    assert ax.get_legend().get_lines()[0].get_linewidth() == 1
    assert ax.get_legend().get_lines()[1].get_linewidth() == 2