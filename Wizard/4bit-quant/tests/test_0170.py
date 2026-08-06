python
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

def test_task_func():
    # Test case 1: Valid input
    image = np.random.rand(10, 10)
    ax, filtered_image = task_func(image, 2)
    assert isinstance(ax, plt.Axes)
    assert isinstance(filtered_image, np.ndarray)

    # Test case 2: Invalid input: image is not a numpy array
    image = [1, 2, 3]
    with pytest.raises(TypeError):
        task_func(image, 2)

    # Test case 3: Invalid input: sigma is not positive
    image = np.random.rand(10, 10)
    with pytest.raises(ValueError):
        task_func(image, -1)