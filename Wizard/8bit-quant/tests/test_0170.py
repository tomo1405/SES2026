python
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def test_task_func():
    # Test case 1: Valid input
    image = np.random.rand(10, 10)
    ax, filtered_image = task_func(image, 2)
    assert isinstance(ax, tuple)
    assert isinstance(filtered_image, np.ndarray)
    assert ax[0].get_title() == 'Original'
    assert ax[1].get_title() == 'Filtered'

    # Test case 2: Invalid input: image is not a numpy array
    image = [1, 2, 3]
    try:
        task_func(image, 2)
    except TypeError as e:
        assert str(e) == "The image must be a numpy array."

    # Test case 3: Invalid input: sigma is not positive
    image = np.random.rand(10, 10)
    try:
        task_func(image, -1)
    except ValueError as e:
        assert str(e) == "Sigma must be positive."