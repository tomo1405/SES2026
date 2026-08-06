import pytest
from src_0996 import task_func

# Test cases for task_func

def test_task_func_valid_file():
    # Assuming the file exists and is a valid CSV
    file_path = "path/to/valid/file.csv"
    plot_path = "path/to/plot.png"
    mean, median, plot_path_result = task_func(file_path, plot_path)
    
    assert isinstance(mean, float)
    assert isinstance(median, float)
    assert isinstance(plot_path_result, str)
    assert os.path.isfile(plot_path_result)

def test_task_func_invalid_file():
    file_path = "path/to/nonexistent/file.csv"
    plot_path = "path/to/plot.png"
    with pytest.raises(FileNotFoundError):
        task_func(file_path, plot_path)

def test_task_func_empty_file():
    # Assuming the file exists but is empty
    file_path = "path/to/empty/file.csv"
    plot_path = "path/to/plot.png"
    mean, median, plot_path_result = task_func(file_path, plot_path)
    
    assert np.isnan(mean)
    assert np.isnan(median)
    assert os.path.isfile(plot_path_result)