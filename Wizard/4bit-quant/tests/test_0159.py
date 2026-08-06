python
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
    url_str = "https://jsonplaceholder.typicode.com/todos/1"
    file_path = "test.json.gz"

    # Test if the function returns the correct file path
    assert task_func(url_str, file_path) == file_path

    # Test if the function downloads the correct data
    response = urllib.request.urlopen(url_str)
    data = response.read().decode()
    json_data = json.loads(data)

    with gzip.open(file_path, 'rb') as f_in:
        downloaded_data = f_in.read().decode()

    assert json.loads(downloaded_data) == json_data

    # Test if the function creates a valid gzip file
    with gzip.open(file_path, 'rb') as f_in:
        try:
            gzip.decompress(f_in.read())
        except OSError:
            assert False, "File is not a valid gzip file"