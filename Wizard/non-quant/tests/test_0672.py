python
import os
import random
import json
import pytest

def task_func(directory, n):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(n):
        filename = str(i) + ".json"
        filepath = os.path.join(directory, filename)

        with open(filepath, 'w') as file:
            json.dump({'number': random.randint(1, 100)}, file)
            file.seek(0)

    return directory

def test_task_func():
    directory = 'test_directory'
    n = 10

    task_func(directory, n)

    assert os.path.exists(directory)
    assert len(os.listdir(directory)) == n

    for i in range(n):
        filename = str(i) + ".json"
        filepath = os.path.join(directory, filename)

        with open(filepath, 'r') as file:
            data = json.load(file)
            assert 'number' in data
            assert isinstance(data['number'], int)
            assert 1 <= data['number'] <= 100