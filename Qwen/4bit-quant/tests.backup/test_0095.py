import pytest
from src_0095 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.mark.parametrize("mean, std_dev, num_samples", [
    (0, 1, 1000),
    (5, 2, 500),
    (-1, 0.5, 2000)
])
def test_task_func(mean, std_dev, num_samples):
    samples, fig = task_func(mean, std_dev, num_samples)
    
    # Check if samples are of the correct shape
    assert samples.shape == (num_samples,), f"Expected {num_samples} samples, got {samples.shape[0]}"
    
    # Check if the mean and standard deviation of the samples are close to the input parameters
    assert np.isclose(np.mean(samples), mean, atol=0.1), f"Mean mismatch: expected {mean}, got {np.mean(samples)}"
    assert np.isclose(np.std(samples), std_dev, atol=0.1), f"Standard deviation mismatch: expected {std_dev}, got {np.std(samples)}"
    
    # Check if the figure is created
    assert isinstance(fig, plt.Figure), "Figure is not of type plt.Figure"
    
    # Close the figure to prevent it from displaying
    plt.close(fig)