import pytest
from src_1002 import task_func

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    ax = task_func(csv_file_path)
    assert ax is not None
    # Add more assertions to test the functionality of the function
    # For example, you can check if the plot title, xlabel, and ylabel are as expected
    # You can also check if the plot looks as expected by using a library like matplotlib.image