import matplotlib.pyplot as plt
from src_0292 import task_func


def test_task_func():
    # Test that the function runs without errors
    mu = 0
    sigma = 1
    result = task_func(mu, sigma)
    
    # Check if the result is a matplotlib.mpl_connectors.Collection
    assert isinstance(result, plt.cm.ScalarMappable), "The result should be a matplotlib.mpl_connectors.Collection"

    # Check if the plot has been created
    assert plt.gca().has_lines, "The plot should have lines"

    # Check if the colorbar has been added
    assert len(plt.gcf().axes) == 2, "The figure should have two axes (one for the plot and one for the colorbar)"

    # Reset the plot to avoid side effects in other tests
    plt.close('all')