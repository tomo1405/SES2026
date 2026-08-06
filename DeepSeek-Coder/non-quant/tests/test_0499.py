import pytest
from src_0499 import task_func
import xmltodict
import json

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func("", True, "test.json")

def test_task_func_valid_input():
    result = task_func("<xml>example</xml>", False, "test.json")
    assert isinstance(result, dict), "The result should be a dictionary"

def test_task_func_save_json():
    task_func("<xml>example</xml>", True, "test.json")
    with open("test.json", "r") as file:
        content = json.load(file)
    assert isinstance(content, dict), "The JSON file should contain a dictionary"