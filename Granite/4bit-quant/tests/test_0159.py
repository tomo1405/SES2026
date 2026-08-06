import json
import urllib.request
import urllib.parse
import gzip
import pytest

def task_func(url_str, file_path):
    response = urllib.request.urlopen(url_str)
    data = response.read().decode()
    json_data = json.loads(data)

    with gzip.open(file_path, 'wb') as f_out:
        f_out.write(json.dumps(json_data).encode())

    return file_path

def test_task_func():
    url_str = "https://jsonplaceholder.typicode.com/posts"
    file_path = "test_file.json.gz"
    expected_output = "test_file.json.gz"

    actual_output = task_func(url_str, file_path)

    assert actual_output == expected_output