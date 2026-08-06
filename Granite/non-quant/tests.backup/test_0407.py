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
    expected_original_img_array = np.array(...)
    expected_rotated_img_array = np.array(...)
    
    original_img_array, rotated_img_array = task_func(img_path, angle)
    
    assert original_img_array.all() == expected_original_img_array.all()
    assert rotated_img_array.all() == expected_rotated_img_array.all()

if __name__ == "__main__":
    pytest.main()