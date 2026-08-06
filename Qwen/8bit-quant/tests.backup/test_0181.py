import pytest
from src_0181 import task_func
from PIL import Image
import numpy as np
import os
from io import BytesIO

def create_test_image():
    # Create a simple test image
    image = Image.new('RGB', (100, 100), color = 'red')
    return image

def save_image_to_file(image):
    # Save the test image to a temporary file
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

def test_task_func():
    # Create a test image
    test_image = create_test_image()
    img_byte_arr = save_image_to_file(test_image)

    # Write the image to a temporary file
    temp_image_path = "temp_test_image.png"
    with open(temp_image_path, 'wb') as f:
        f.write(img_byte_arr.getvalue())

    try:
        # Call the function with the path to the test image
        results = task_func(temp_image_path)

        # Check if the results are as expected
        assert len(results) == 4, "The number of results should match the number of scale factors."
        for ax, scaled_img_arr in results:
            assert isinstance(ax, plt.Axes), "Each result should contain a matplotlib Axes object."
            assert isinstance(scaled_img_arr, np.ndarray), "Each result should contain a numpy array."

    finally:
        # Clean up the temporary file
        os.remove(temp_image_path)

def test_task_func_non_existent_file():
    # Test the function with a non-existent file path
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.png")