import json

import pytest
from src_0499 import task_func


def test_task_func_empty_string():
    with pytest.raises(ValueError):
        task_func("", True, "test.json")

def test_task_func_whitespace_string():
    with pytest.raises(ValueError):
        task_func("   ", True, "test.json")

def test_task_func_valid_xml():
    xml_string = "<root><child>value</child></root>"
    my_dict = task_func(xml_string, True, "test.json")
    assert my_dict == {"root": {"child": "value"}}

def test_task_func_invalid_xml():
    xml_string = "<root><child>value</root>"
    with pytest.raises(ValueError):
        task_func(xml_string, True, "test.json")

def test_task_func_save_json():
    xml_string = "<root><child>value</child></root>"
    task_func(xml_string, True, "test.json")
    with open("test.json", "r") as json_file:
        json_data = json.load(json_file)
    assert json_data == {"root": {"child": "value"}}