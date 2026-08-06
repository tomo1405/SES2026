import pytest
from src_0407 import task_func
from PIL import Image
import numpy as np
import os

# Mocking the os.path.exists function to simulate file existence
class MockOsPathExists:
    def __init__(self, exists):
        self.exists = exists

    def __call__(self, path):
        return self.exists

# Mocking the Image.open function to simulate image opening
class MockImageOpen:
    def __init__(self, image_data):
        self.image_data = image_data

    def rotate(self, angle, expand):
        # Simulate rotation by returning the same image data
        return Image.fromarray(self.image_data)

    def __array__(self):
        return self.image_data

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_path.jpg", 90)
    assert str(excinfo.value) == "No file found at non_existent_path.jpg"

def test_task_func_valid_image():
    # Mock the os.path.exists function to return True
    os.path.exists = MockOsPathExists(True)
    
    # Create a mock image data
    image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    
    # Mock the Image.open function to return the mock image data
    Image.open = lambda x: MockImageOpen(image_data)
    
    # Call the function with a valid image path and angle
    original_img_array, rotated_img_array = task_func("valid_image_path.jpg", 90)
    
    # Check that the returned arrays are equal to the mock image data
    assert np.array_equal(original_img_array, image_data)
    assert np.array_equal(rotated_img_array, image_data)