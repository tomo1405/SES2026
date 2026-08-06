import pytest
from src_0673 import task_func
import os
import tempfile

def test_task_func():
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_file:
        temp_filename = temp_file.name
        temp_file.write("name,age\nAlice,30\nBob,25")
        temp_file.flush()

    # Call the function
    result = task_func(temp_filename)

    # Check if the function returned the correct filename
    assert result == temp_filename

    # Read the content of the file after processing
    with open(temp_filename, 'r') as file:
        content = file.read()

    # Expected content after reversing the rows
    expected_content = "name,age\nBob,25\nAlice,30"

    # Check if the content is as expected
    assert content == expected_content

    # Clean up the temporary file
    os.remove(temp_filename)