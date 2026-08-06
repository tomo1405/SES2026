import pytest
from src_0426 import task_func
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_default_paths():
    # Create a temporary image file
    temp_image_path = 'temp_image.jpg'
    temp_histogram_path = 'temp_histogram.png'
    
    # Create a simple black image
    img = np.zeros((100, 100), dtype=np.uint8)
    cv2.imwrite(temp_image_path, img)
    
    try:
        axes = task_func(temp_image_path, temp_histogram_path)
        
        # Check if the histogram image is created
        assert os.path.exists(temp_histogram_path), "Histogram image not created"
        
        # Check if the axes object is returned
        assert isinstance(axes, plt.Axes), "Return value is not a matplotlib Axes object"
        
    finally:
        # Clean up temporary files
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)
        if os.path.exists(temp_histogram_path):
            os.remove(temp_histogram_path)

def test_task_func_custom_paths():
    # Create a temporary image file
    temp_image_path = 'custom_image.jpg'
    temp_histogram_path = 'custom_histogram.png'
    
    # Create a simple black image
    img = np.zeros((100, 100), dtype=np.uint8)
    cv2.imwrite(temp_image_path, img)
    
    try:
        axes = task_func(temp_image_path, temp_histogram_path)
        
        # Check if the histogram image is created
        assert os.path.exists(temp_histogram_path), "Histogram image not created"
        
        # Check if the axes object is returned
        assert isinstance(axes, plt.Axes), "Return value is not a matplotlib Axes object"
        
    finally:
        # Clean up temporary files
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)
        if os.path.exists(temp_histogram_path):
            os.remove(temp_histogram_path)

def test_task_func_non_existent_image():
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_image.jpg')

def test_task_func_color_image():
    # Create a temporary color image file
    temp_image_path = 'color_image.jpg'
    temp_histogram_path = 'color_histogram.png'
    
    # Create a simple color image
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite(temp_image_path, img)
    
    try:
        axes = task_func(temp_image_path, temp_histogram_path)
        
        # Check if the histogram image is created
        assert os.path.exists(temp_histogram_path), "Histogram image not created"
        
        # Check if the axes object is returned
        assert isinstance(axes, plt.Axes), "Return value is not a matplotlib Axes object"
        
    finally:
        # Clean up temporary files
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)
        if os.path.exists(temp_histogram_path):
            os.remove(temp_histogram_path)