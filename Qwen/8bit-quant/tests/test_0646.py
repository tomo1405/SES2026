import pytest
from src_0646 import task_func
import os
import pandas as pd

# Helper function to create a temporary file with specified content
def create_temp_file(content: str) -> str:
    temp_file = "temp_test_file.csv"
    with open(temp_file, 'w') as file:
        file.write(content)
    return temp_file

# Helper function to remove the temporary file
def remove_temp_file(filename: str):
    if os.path.exists(filename):
        os.remove(filename)

def test_task_func_file_not_found():
    filename = "non_existent_file.csv"
    with pytest.raises(FileNotFoundError):
        task_func(filename)

def test_task_func_empty_file():
    filename = create_temp_file("")
    result_df = task_func(filename)
    assert result_df.empty
    assert result_df.columns.size == 0
    remove_temp_file(filename)

def test_task_func_non_empty_file():
    data = "name,age\nAlice,30\nBob,25"
    filename = create_temp_file(data)
    expected_df = pd.DataFrame({
        "name": ["Alice", "Bob"],
        "age": [30, 25]
    })
    result_df = task_func(filename)
    pd.testing.assert_frame_equal(result_df, expected_df)
    assert os.stat(filename).st_size == 0  # Ensure the file is empty after reading
    remove_temp_file(filename)

def test_task_func_file_permissions():
    # This test assumes that the user running the tests has write permissions
    filename = create_temp_file("test_data")
    os.chmod(filename, 0o444)  # Make the file read-only
    with pytest.raises(PermissionError):
        task_func(filename)
    os.chmod(filename, 0o644)  # Restore write permissions
    remove_temp_file(filename)