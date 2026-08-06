python
import pytest
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def task_func(img_path, angle):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")
    
    img = Image.open(img_path)
    rotated_img = img.rotate(angle,expand=True)

    # Convert images to numpy arrays
    original_img_array = np.array(img)
    rotated_img_array = np.array(rotated_img)
    
    # Display original and rotated images side by side
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(rotated_img)
    plt.title('Rotated Image')

    return original_img_array, rotated_img_array

def test_task_func():
    # Test case 1: Valid input
    img_path = "test_image.jpg"
    angle = 90
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert original_img_array.shape == rotated_img_array.shape
    assert original_img_array.shape == (225, 400, 3)
    assert rotated_img_array.shape == (400, 225, 3)

    # Test case 2: Invalid input (file not found)
    img_path = "invalid_file.jpg"
    angle = 90
    with pytest.raises(FileNotFoundError):
        task_func(img_path, angle)

    # Test case 3: Invalid input (angle not a number)
    img_path = "test_image.jpg"
    angle = "not_a_number"
    with pytest.raises(ValueError):
        task_func(img_path, angle)