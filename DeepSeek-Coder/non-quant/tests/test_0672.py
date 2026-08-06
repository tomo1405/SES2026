import pytest
from src_0672 import task_func
import os
import random
import json

def test_task_func():
    # Test with a valid directory and n
    directory = "test_dir"
    n = 5
    result = task_func(directory, n)
    assert os.path.exists(directory), "Directory should be created"
    assert len(os.listdir(directory)) == n, "Number of files should be equal to n"
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            assert 'number' in data, "JSON should contain 'number' key"
            assert isinstance(data['number'], int), "Number should be an integer"
            assert 1 <= data['number'] <= 100, "Number should be between 1 and 100"
    os.rmdir(directory)

if __name__ == "__main__":
    pytest.main()