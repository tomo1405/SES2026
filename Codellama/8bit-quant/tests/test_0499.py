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
    expected_dict = {"root": {"child": "value"}}
    assert task_func(xml_string, False, None) == expected_dict

def test_task_func_valid_xml_with_json_save():
    xml_string = "<root><child>value</child></root>"
    expected_dict = {"root": {"child": "value"}}
    assert task_func(xml_string, True, "test.json") == expected_dict
    with open("test.json", "r") as json_file:
        assert json.load(json_file) == expected_dict