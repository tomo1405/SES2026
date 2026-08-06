python
import numpy as np
import matplotlib.pyplot as plt
import pytest

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5

def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    normal_data = np.random.normal(size=num_samples)
    outliers = np.random.uniform(low=-10, high=10, size=num_outliers)
    data = np.concatenate([normal_data, outliers]) if num_samples > 0 else outliers

    # Identify outliers using IQR (only if there is normal data)
    outliers_detected = np.array([])
    if num_samples > 0:
        q75, q25 = np.percentile(normal_data, [75, 25])
        iqr = q75 - q25
        lower_bound = q25 - (iqr * 1.5)
        upper_bound = q75 + (iqr * 1.5)
        outliers_detected = data[(data < lower_bound) | (data > upper_bound)]

    # Plot histogram
    _, ax = plt.subplots()
    ax.hist(data, bins=30)

    return data, outliers_detected, ax

# Test task_func()
def test_task_func():
    # Test with default parameters
    data, outliers_detected, ax = task_func()
    assert len(data) == NUM_SAMPLES + NUM_OUTLIERS
    assert len(outliers_detected) == NUM_OUTLIERS
    assert ax.get_title() == 'Histogram'

    # Test with custom parameters
    data, outliers_detected, ax = task_func(num_samples=50, num_outliers=2)
    assert len(data) == 50 + 2
    assert len(outliers_detected) == 2
    assert ax.get_title() == 'Histogram'

    # Test with empty data
    data, outliers_detected, ax = task_func(num_samples=0, num_outliers=2)
    assert len(data) == 2
    assert len(outliers_detected) == 2
    assert ax.get_title() == 'Histogram'

    # Test with all outliers
    data, outliers_detected, ax = task_func(num_samples=0, num_outliers=100)
    assert len(data) == 100
    assert len(outliers_detected) == 100
    assert ax.get_title() == 'Histogram'

    # Test with all normal data
    data, outliers_detected, ax = task_func(num_samples=100, num_outliers=0)
    assert len(data) == 100
    assert len(outliers_detected) == 0
    assert ax.get_title() == 'Histogram'

    # Test with all normal data and outliers
    data, outliers_detected, ax = task_func(num_samples=100, num_outliers=100)
    assert len(data) == 200
    assert len(outliers_detected) == 100
    assert ax.get_title() == 'Histogram'

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(num_samples=-1)
    with pytest.raises(ValueError):
        task_func(num_outliers=-1)
    with pytest.raises(ValueError):
        task_func(num_samples=101)
    with pytest.raises(ValueError):
        task_func(num_outliers=101)