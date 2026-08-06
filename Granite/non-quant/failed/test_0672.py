import os
import random
import json
import pytest
from src_0672 import task_func

def test_task_func():
    directory = 'test_directory'
    n = 5
    expected_output = 'test_directory'
    actual_output = task_func(directory, n)
    assert actual_output == expected_output
    assert os.path.exists(directory)
    assert len(os.listdir(directory)) == n
    for i in range(n):
        filename = str(i) + ".json"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            assert isinstance(data, dict)
            assert 'number' in data
            assert 1 <= data['number'] <= 100