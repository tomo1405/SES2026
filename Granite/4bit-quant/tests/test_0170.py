import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
def task_func(image, sigma=2):
    if not isinstance(image, np.ndarray):
        raise TypeError("The image must be a numpy array.")
    if sigma <= 0:
        raise ValueError("Sigma must be positive.")

    filtered_image = gaussian_filter(image, sigma=sigma)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].set_title('Original')

    ax[1].imshow(filtered_image, cmap=plt.cm.gray)
    ax[1].set_title('Filtered')

    return ax, filtered_image
import pytest
def test_task_func():
    image = np.random.rand(100, 100)
    sigma = 2
    ax, filtered_image = task_func(image, sigma)
    assert isinstance(ax, np.ndarray)
    assert isinstance(filtered_image, np.ndarray)
    assert ax.shape == (2, 100, 100)
    assert filtered_image.shape == (100, 100)
def test_task_func_invalid_image():
    image = "not an array"
    sigma = 2
    with pytest.raises(TypeError):
        task_func(image, sigma)
def test_task_func_invalid_sigma():
    image = np.random.rand(100, 100)
    sigma = -1
    with pytest.raises(ValueError):
        task_func(image, sigma)