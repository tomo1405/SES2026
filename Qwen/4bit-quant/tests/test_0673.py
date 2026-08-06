import pytest
from src_0673 import task_func
import os
import tempfile

def test_task_func_with_valid_csv():
    # Create a temporary CSV file with some content
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', newline='') as temp_file:
        temp_file.write("Name,Age\nAlice,30\nBob,25")
        temp_file.flush()
        temp_filename = temp_file.name

    # Call the function with the temporary file
    result = task_func(temp_filename)

    # Check if the function returns the correct filename
    assert result == temp_filename

    # Read the contents of the file after the function call
    with open(temp_filename, 'r') as file:
        content = file.read()

    # Check if the contents have been reversed
    expected_content = "Name,Age\nBob,25\nAlice,30"
    assert content == expected_content

    # Clean up the temporary file
    os.remove(temp_filename)

def test_task_func_with_non_existent_file():
    # Use a non-existent file path
    non_existent_filename = "non_existent.csv"

    # Call the function with the non-existent file
    result = task_func(non_existent_filename)

    # Check if the function returns the correct filename
    assert result == non_existent_filename

    # Check if the file was not created
    assert not os.path.exists(non_existent_filename)

def test_task_func_with_empty_csv():
    # Create a temporary empty CSV file
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', newline='') as temp_file:
        temp_filename = temp_file.name

    # Call the function with the empty file
    result = task_func(temp_filename)

    # Check if the function returns the correct filename
    assert result == temp_filename

    # Read the contents of the file after the function call
    with open(temp_filename, 'r') as file:
        content = file.read()

    # Check if the contents are still empty
    assert content == ""

    # Clean up the temporary file
    os.remove(temp_filename)

def test_task_func_with_single_row_csv():
    # Create a temporary CSV file with a single row
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', newline='') as temp_file:
        temp_file.write("Name,Age\nAlice,30")
        temp_file.flush()
        temp_filename = temp_file.name

    # Call the function with the single row file
    result = task_func(temp_filename)

    # Check if the function returns the correct filename
    assert result == temp_filename

    # Read the contents of the file after the function call
    with open(temp_filename, 'r') as file:
        content = file.read()

    # Check if the contents are still the same
    expected_content = "Name,Age\nAlice,30"
    assert content == expected_content

    # Clean up the temporary file
    os.remove(temp_filename)