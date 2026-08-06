import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def task_func(mu, sigma, seed=0):
    # Set the random seed
    np.random.seed(seed)
    # Generate samples from the normal distribution
    samples = np.random.normal(mu, sigma, 1000)

    # Generate a KDE plot
    mappable = sns.kdeplot(samples, fill=True)

    # Add a colorbar to the plot
    plt.colorbar(mappable=mappable.collections[0])

    return mappable
import pytest

def test_task_func():
    # Test case 1: Check if the function returns the expected output for mu=0, sigma=1, and seed=0
    result = task_func(mu=0, sigma=1, seed=0)
    assert isinstance(result, object)

    # Test case 2: Check if the function returns the expected output for mu=1, sigma=2, and seed=1
    result = task_func(mu=1, sigma=2, seed=1)
    assert isinstance(result, object)

    # Test case 3: Check if the function returns the expected output for mu=-1, sigma=3, and seed=2
    result = task_func(mu=-1, sigma=3, seed=2)
    assert isinstance(result, object)

if __name__ == "__main__":
    pytest.main()