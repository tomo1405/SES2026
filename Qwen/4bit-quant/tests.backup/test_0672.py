import pytest
from src_0672 import task_func
import os
import json

def test_task_func(tmpdir):
    # Create a temporary directory
    temp_dir = tmpdir.mkdir("test_directory")
    n = 5

    # Call the function
    result = task_func(str(temp_dir), n)

    # Check if the directory exists
    assert os.path.exists(result)

    # Check if the correct number of files are created
    files = os.listdir(result)
    assert len(files) == n

    # Check if each file contains valid JSON data
    for i in range(n):
        filename = f"{i}.json"
        filepath = os.path.join(result, filename)
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