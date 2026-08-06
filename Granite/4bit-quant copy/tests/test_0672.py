import os
import random
import json
import pytest

from src_0672 import task_func

def test_task_func():
    directory = "test_directory"
    n = 5
    expected_output = "test_directory"

    # Test when directory does not exist
    if os.path.exists(directory):
        os.rmdir(directory)
    assert not os.path.exists(directory)

    output = task_func(directory, n)
    assert output == expected_output
    assert os.path.exists(directory)
    assert len(os.listdir(directory)) == n

    for i in range(n):
        filename = str(i) + ".json"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            assert data['number'] >= 1 and data['number'] <= 100

    # Clean up
    os.rmdir(directory)

if __name__ == "__main__":
    pytest.main()