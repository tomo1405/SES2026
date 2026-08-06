import pytest
from src_0407 import task_func
from PIL import Image
import numpy as np
import os
import tempfile

def test_task_func_valid_image():
    # Create a temporary image file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        img_path = temp_file.name
        img = Image.new('RGB', (100, 100), color='red')
        img.save(img_path)
        
        try:
            original_array, rotated_array = task_func(img_path, 90)
            
            assert isinstance(original_array, np.ndarray)
            assert isinstance(rotated_array, np.ndarray)
            assert original_array.shape == (100, 100, 3)
            assert rotated_array.shape == (100, 100, 3)
        finally:
            os.remove(img_path)

def test_task_func_nonexistent_image():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("nonexistent_image.png", 90)
    assert "No file found at nonexistent_image.png" in str(excinfo.value)

def test_task_func_zero_angle():
    # Create a temporary image file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        img_path = temp_file.name
        img = Image.new('RGB', (100, 100), color='blue')
        img.save(img_path)
        
        try:
            original_array, rotated_array = task_func(img_path, 0)
            
            assert isinstance(original_array, np.ndarray)
            assert isinstance(rotated_array, np.ndarray)
            assert np.array_equal(original_array, rotated_array)
        finally:
            os.remove(img_path)

def test_task_func_negative_angle():
    # Create a temporary image file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        img_path = temp_file.name
        img = Image.new('RGB', (100, 100), color='green')
        img.save(img_path)
        
        try:
            original_array, rotated_array = task_func(img_path, -90)
            
            assert isinstance(original_array, np.ndarray)
            assert isinstance(rotated_array, np.ndarray)
            assert original_array.shape == (100, 100, 3)
            assert rotated_array.shape == (100, 100, 3)
        finally:
            os.remove(img_path)