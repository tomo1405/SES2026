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
    img_path = "path/to/image.jpg"
    angle = 45
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert original_img_array.shape == rotated_img_array.shape, "The original and rotated images should have the same shape"
    assert original_img_array.dtype == rotated_img_array.dtype, "The original and rotated images should have the same data type"
    assert original_img_array.sum() != rotated_img_array.sum(), "The original and rotated images should have different pixel values"

if __name__ == "__main__":
    pytest.main()