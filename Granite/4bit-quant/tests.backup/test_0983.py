import pytest
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(df, column, bins=30, density=True, alpha=0.6, color="g", seed=None):
    if seed is not None:
        np.random.seed(seed)

    data = df[column]
    mu, std = norm.fit(data)

    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, density=density, alpha=alpha, color=color)

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, "k", linewidth=2)

    title = f"Normal Fit for '{column}'"
    ax.set_title(title)
    ax.set_ylabel("Density")
    ax.set_xlabel(column)

    return ax

def test_task_func():
    # Test case 1: Test with default parameters
    df = pd.DataFrame({'column': np.random.normal(size=100)})
    ax = task_func(df, 'column')
    assert ax.get_title() == "Normal Fit for 'column'"
    assert ax.get_xlabel() == 'column'
    assert ax.get_ylabel() == 'Density'

    # Test case 2: Test with custom parameters
    df = pd.DataFrame({'column': np.random.normal(size=100)})
    ax = task_func(df, 'column', bins=50, density=False, alpha=0.8, color='r', seed=42)
    assert ax.get_title() == "Normal Fit for 'column'"
    assert ax.get_xlabel() == 'column'
    assert ax.get_ylabel() == 'Frequency'

if __name__ == '__main__':
    pytest.main()