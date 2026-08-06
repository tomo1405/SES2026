import pytest
from src_0159 import task_func

def test_task_func():
    url_str = "https://www.example.com/data.json"
    file_path = "test_data.json.gz"

    with pytest.raises(ValueError):
        task_func(url_str, file_path)

    assert task_func(url_str, file_path) == file_path