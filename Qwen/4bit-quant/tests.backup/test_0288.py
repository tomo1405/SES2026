import pytest
from src_0288 import task_func
import os
import json
import tempfile

def test_task_func():
    # Create a temporary directory and files for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some text files in the temporary directory
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        with open(file1_path, 'w') as f:
            f.write("hello world hello")
        with open(file2_path, 'w') as f:
            f.write("world world")

        # Define the output file path
        output_file_path = os.path.join(temp_dir, 'output.json')

        # Call the function
        total_words = task_func(output_file_path, temp_dir)

        # Check if the total words count is correct
        assert total_words == 5

        # Check if the JSON file was created correctly
        with open(output_file_path, 'r') as f:
            data = json.load(f)
        assert data == {'hello': 2, 'world': 3}

# Run the test
if __name__ == "__main__":
    pytest.main()