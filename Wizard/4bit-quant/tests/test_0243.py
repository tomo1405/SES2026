python
import cv2
import matplotlib.pyplot as plt
import pytest

def task_func(image_path, kernel_size):
    if kernel_size <= 0 or not isinstance(kernel_size, int):
        raise ValueError("kernel_size must be a positive integer")
    
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"No image found at {image_path}")
    except FileNotFoundError as e:
        raise e

    blurred_image = cv2.blur(image, (kernel_size, kernel_size))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), ax1.set_title('Original')
    ax1.set_xticks([]), ax1.set_yticks([])
    ax2.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)), ax2.set_title('Blurred')
    ax2.set_xticks([]), ax2.set_yticks([])
    # plt.show()

    return blurred_image, ax1, ax2

def test_task_func():
    # Test case 1: Valid input
    image_path = "test_image.jpg"
    kernel_size = 3
    expected_output = (blurred_image, ax1, ax2) = task_func(image_path, kernel_size)
    assert isinstance(blurred_image, np.ndarray)
    assert isinstance(ax1, matplotlib.axes.Axes)
    assert isinstance(ax2, matplotlib.axes.Axes)

    # Test case 2: Invalid input (kernel_size <= 0)
    with pytest.raises(ValueError):
        task_func(image_path, 0)

    # Test case 3: Invalid input (not a string)
    with pytest.raises(TypeError):
        task_func(123, kernel_size)

    # Test case 4: Invalid input (file not found)
    with pytest.raises(FileNotFoundError):
        task_func("invalid_file.jpg", kernel_size)