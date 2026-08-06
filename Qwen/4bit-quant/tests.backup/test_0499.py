import pytest
from src_0499 import task_func
import xmltodict
import json
import os

def test_task_func_with_valid_xml():
    xml_string = "<root><child>value</child></root>"
    result = task_func(xml_string, False, None)
    expected_dict = {'root': {'child': 'value'}}
    assert result == expected_dict

def test_task_func_with_empty_xml():
    with pytest.raises(ValueError) as excinfo:
        task_func("", False, None)
    assert str(excinfo.value) == "The input XML string is empty or contains only whitespace."

def test_task_func_with_whitespace_only_xml():
    with pytest.raises(ValueError) as excinfo:
        task_func("   ", False, None)
    assert str(excinfo.value) == "The input XML string is empty or contains only whitespace."

def test_task_func_with_save_json_true():
    xml_string = "<root><child>value</child></root>"
    json_file_path = "test_output.json"
    task_func(xml_string, True, json_file_path)
    with open(json_file_path, 'r') as json_file:
        content = json.load(json_file)
    expected_dict = {'root': {'child': 'value'}}
    assert content == expected_dict
    os.remove(json_file_path)

def test_task_func_with_save_json_false():
    xml_string = "<root><child>value</child></root>"
    json_file_path = "test_output.json"
    task_func(xml_string, False, json_file_path)
    assert not os.path.exists(json_file_path)