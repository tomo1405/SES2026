import pytest
from src_0427 import task_func

def test_task_func_invalid_threshold_type():
    with pytest.raises(ValueError, match="Threshold must be an integer between 0 and 255."):
        task_func(threshold='128')

def test_task_func_threshold_out_of_range():
    with pytest.raises(ValueError, match="Threshold must be an integer between 0 and 255."):
        task_func(threshold=-1)
    with pytest.raises(ValueError, match="Threshold must be an integer between 0 and 255."):
        task_func(threshold=256)

def test_task_func_non_existent_image_path():
    with pytest.raises(FileNotFoundError, match="No image found at non_existent.jpg"):
        task_func(image_path='non_existent.jpg')

def test_task_func_valid_input(tmpdir):
    # Create a temporary directory and add a sample image
    tmp_dir = tmpdir.mkdir("test_images")
    sample_image_path = tmp_dir.join("sample_image.jpg")
    sample_image_path.write_binary(open("path_to_real_image.jpg", "rb").read())

    original_img, binary_img = task_func(str(sample_image_path), threshold=128)

    assert isinstance(original_img, np.ndarray)
    assert isinstance(binary_img, np.ndarray)
    assert binary_img.dtype == 'uint8'
    assert os.path.exists('binary_image.jpg')

def test_task_func_binary_image_content(tmpdir):
    # Create a temporary directory and add a sample image
    tmp_dir = tmpdir.mkdir("test_images")
    sample_image_path = tmp_dir.join("sample_image.jpg")
    sample_image_path.write_binary(open("path_to_real_image.jpg", "rb").read())

    original_img, binary_img = task_func(str(sample_image_path), threshold=128)

    # Check if the binary image is correctly generated
    assert np.all((binary_img == 0) | (binary_img == 255))