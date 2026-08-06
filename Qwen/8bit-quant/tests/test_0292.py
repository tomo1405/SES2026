import matplotlib.pyplot as plt
import pytest
import seaborn as sns
from src_0292 import task_func


def test_task_func():
    mu = 0
    sigma = 1
    mappable = task_func(mu, sigma)

    # Check that the returned object is a seaborn.axisgrid._KDEPlotter
    assert isinstance(mappable, sns.axisgrid._KDEPlotter)

    # Check that the plot has been created
    fig = plt.gcf()
    assert len(fig.axes) == 1

    # Check that the colorbar has been added
    assert len(fig.axes[0].collections) == 1
    assert len(fig.axes[1].collections) == 1  # Colorbar collection

    # Reset the plot for the next test
    plt.clf()

# Run the test
if __name__ == "__main__":
    pytest.main()