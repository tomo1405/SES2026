import pytest
from src_0499 import task_func

def test_task_func():
    s = "<xml><tag>value</tag></xml>"
    save_json = True
    json_file_path = "output.json"
    expected_output = {"xml": {"tag": "value"}}

    with pytest.raises(ValueError):
        task_func("", save_json, json_file_path)

    assert task_func(s, save_json, json_file_path) == expected_output