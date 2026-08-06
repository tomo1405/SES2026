import matplotlib.pyplot as plt
import numpy as np
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
    image = np.random.rand(100, 100)
    sigma = 2
    expected_output = (ax, filtered_image)
    actual_output = task_func(image, sigma)
    assert actual_output == expected_output, "Task function output does not match expected output."
test_task_func()