import json
import os

from src_0672 import task_func


def test_task_func():
    directory = task_func("test_directory", 5)
    assert os.path.exists(directory)

    for i in range(5):
        filename = str(i) + ".json"
        filepath = os.path.join(directory, filename)
        assert os.path.exists(filepath)

        with open(filepath, 'r') as file:
            data = json.load(file)
            assert data['number'] >= 1 and data['number'] <= 100