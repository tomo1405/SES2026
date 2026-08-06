import pytest
from src_0672 import task_func
import os
import json

def test_task_func(tmpdir):
    # Create a temporary directory using pytest's tmpdir fixture
    temp_dir = tmpdir.strpath

    # Define the number of JSON files to create
    n = 5

    # Call the task_func function
    result = task_func(temp_dir, n)

    # Check if the result is the same as the input directory
    assert result == temp_dir

    # Check if the correct number of files were created
    files = os.listdir(temp_dir)
    assert len(files) == n

    # Check if each file is a valid JSON file and contains the correct structure
    for i in range(n):
        filename = f"{i}.json"
        filepath = os.path.join(temp_dir, filename)
        assert os.path.isfile(filepath)

        with open(filepath, 'r') as file:
            data = json.load(file)
            assert isinstance(data, dict)
            assert 'number' in data
            assert isinstance(data['number'], int)
            assert 1 <= data['number'] <= 100

# Run the tests
if __name__ == "__main__":
    pytest.main()