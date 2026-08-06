import pytest
from src_1054 import task_func

# Test 1: Test that the function returns None when the file is not found
def test_file_not_found():
    file_path = "path/to/file.csv"
    save_path = None
    result = task_func(file_path, save_path)
    assert result is None

# Test 2: Test that the function raises a FileNotFoundError when the file is not found
def test_file_not_found_error():
    file_path = "path/to/file.csv"
    save_path = None
    with pytest.raises(FileNotFoundError):
        task_func(file_path, save_path)

# Test 3: Test that the function returns a matplotlib.axes.Axes object when the file is found
def test_axes_object():
    file_path = "path/to/file.csv"
    save_path = None
    result = task_func(file_path, save_path)
    assert isinstance(result, matplotlib.axes.Axes)

# Test 4: Test that the function saves the plot to the specified file path when the save_path argument is provided
def test_save_path():
    file_path = "path/to/file.csv"
    save_path = "path/to/save.png"
    result = task_func(file_path, save_path)
    assert os.path.exists(save_path)

# Test 5: Test that the function raises an error when the file is not a CSV file
def test_invalid_file_type():
    file_path = "path/to/file.txt"
    save_path = None
    with pytest.raises(ValueError):
        task_func(file_path, save_path)