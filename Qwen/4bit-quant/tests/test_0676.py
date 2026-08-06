import pytest
from src_0676 import task_func
import os
import tempfile

def test_task_func():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Define the number of files to create
        n_files = 5

        # Call the function
        result = task_func(temp_dir, n_files)

        # Check if the returned directory is correct
        assert result == temp_dir

        # Check if the directory exists
        assert os.path.exists(temp_dir)

        # Check if the correct number of files are created
        files_in_directory = os.listdir(temp_dir)
        assert len(files_in_directory) == n_files

        # Check if each file contains a valid integer between 1 and 100
        for i in range(n_files):
            filename = os.path.join(temp_dir, f"file_{i+1}.txt")
            with open(filename, 'r') as file:
                content = file.read()
                assert content.isdigit()
                number = int(content)
                assert 1 <= number <= 100

# Run the tests
if __name__ == "__main__":
    pytest.main()