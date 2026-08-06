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
    kernel_size = 5
    expected_output = (None, None, None)
    try:
        output = task_func(image_path, kernel_size)
        assert output == expected_output
    except Exception as e:
        assert False, f"Test case 1 failed with error: {e}"

    # Test case 2: Invalid input (kernel_size <= 0)
    image_path = "test_image.jpg"
    kernel_size = 0
    expected_output = ValueError("kernel_size must be a positive integer")
    try:
        output = task_func(image_path, kernel_size)
        assert False, f"Test case 2 should have raised a ValueError, but instead returned {output}"
    except ValueError as e:
        assert str(e) == str(expected_output), f"Test case 2 failed with error: {e}"

    # Test case 3: Invalid input (kernel_size not an integer)
    image_path = "test_image.jpg"
    kernel_size = "5"
    expected_output = ValueError("kernel_size must be a positive integer")
    try:
        output = task_func(image_path, kernel_size)
        assert False, f"Test case 3 should have raised a ValueError, but instead returned {output}"
    except ValueError as e:
        assert str(e) == str(expected_output), f"Test case 3 failed with error: {e}"

    # Test case 4: Invalid input (image not found)
    image_path = "invalid_image.jpg"
    kernel_size = 5
    expected_output = FileNotFoundError(f"No image found at {image_path}")
    try:
        output = task_func(image_path, kernel_size)
        assert False, f"Test case 4 should have raised a FileNotFoundError, but instead returned {output}"
    except FileNotFoundError as e:
        assert str(e) == str(expected_output), f"Test case 4 failed with error: {e}"