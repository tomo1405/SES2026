import pytest
from src_0673 import task_func
import os
import tempfile

def test_task_func_with_valid_csv():
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_file:
        temp_file.write("col1,col2\nrow1,row2\nrow3,row4")
        temp_file.flush()
        filename = temp_file.name

        # Call the function
        result = task_func(filename)

        # Check if the function returned the correct filename
        assert result == filename

        # Read the content of the file after processing
        with open(filename, 'r') as file:
            content = file.read()

        # Check if the content is reversed
        expected_content = "col1,col2\nrow3,row4\nrow1,row2"
        assert content == expected_content

    # Clean up the temporary file
    os.remove(filename)

def test_task_func_with_nonexistent_file():
    # Create a non-existent filename
    filename = "non_existent_file.csv"

    # Call the function and capture stderr
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(filename)

    # Check if the correct exception was raised
    assert "No such file or directory" in str(excinfo.value)

def test_task_func_with_empty_file():
    # Create a temporary empty CSV file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_file:
        temp_file.flush()
        filename = temp_file.name

        # Call the function
        result = task_func(filename)

        # Check if the function returned the correct filename
        assert result == filename

        # Read the content of the file after processing
        with open(filename, 'r') as file:
            content = file.read()

        # Check if the content is still empty
        expected_content = ""
        assert content == expected_content

    # Clean up the temporary file
    os.remove(filename)