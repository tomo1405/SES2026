python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)

    # Create a histogram and get the Axes object
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(samples, num_bins, density=True)
    ax.plot(
        bins, 
        1/(sigma * np.sqrt(2 * np.pi)) * \
        np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r'
    )
    bins = (bins[:-1] + bins[1:]) / 2
    model = ols('count ~ bins + np.power(bins, 2)', data={'count': count, 'bins': bins}).fit()
    ax.plot(
        bins, 
        model.params['Intercept'] + model.params['bins'] * bins + \
        model.params['np.power(bins, 2)'] * np.power(bins, 2), linewidth=2, color='g'
    )
    
    return ax

# Test the function with some inputs
def test_task_func():
    ax = task_func(0, 1, seed=0, num_samples=1000, num_bins=30)
    assert ax is not None, "The function should return an Axes object"
    assert len(ax.lines) == 2, "The function should plot two lines"
    assert ax.lines[0].get_color() == 'r', "The first line should be red"
    assert ax.lines[1].get_color() == 'g', "The second line should be green"
    assert ax.get_xlabel() == 'bins', "The x-axis should be labeled 'bins'"
    assert ax.get_ylabel() == 'count', "The y-axis should be labeled 'count'"
    assert ax.get_title() == 'Histogram of Normal Distribution', "The plot should have a title"
    assert ax.get_xlim() == (-3, 3), "The x-axis should be limited to (-3, 3)"
    assert ax.get_ylim() == (0, 0.5), "The y-axis should be limited to (0, 0.5)"
    plt.close()

test_task_func()