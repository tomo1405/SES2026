import gzip
import json
import os

from src_0159 import task_func


def test_task_func():
    url_str = "https://jsonplaceholder.typicode.com/posts"
    file_path = "test_data.json.gz"

    result = task_func(url_str, file_path)

    assert result == file_path
    assert os.path.exists(file_path)

    with gzip.open(file_path, 'rb') as f_in:
        data = json.loads(f_in.read().decode())
        assert isinstance(data, list)
        assert len(data) > 0

    os.remove(file_path)