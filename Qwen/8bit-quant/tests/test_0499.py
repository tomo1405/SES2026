import pytest
from src_0499 import task_func
import xmltodict
import json
import os

def test_task_func_empty_string():
    with pytest.raises(ValueError) as excinfo:
        task_func("", False, None)
    assert str(excinfo.value) == "The input XML string is empty or contains only whitespace."

def test_task_func_whitespace_string():
    with pytest.raises(ValueError) as excinfo:
        task_func("   ", False, None)
    assert str(excinfo.value) == "The input XML string is empty or contains only whitespace."

def test_task_func_valid_xml_no_save():
    xml_str = "<root><child>value</child></root>"
    expected_dict = {'root': {'child': 'value'}}
    result = task_func(xml_str, False, None)
    assert result == expected_dict

def test_task_func_valid_xml_save(tmpdir):
    xml_str = "<root><child>value</child></root>"
    expected_dict = {'root': {'child': 'value'}}
    json_file_path = str(tmpdir / "output.json")
    task_func(xml_str, True, json_file_path)
    
    with open(json_file_path, 'r') as json_file:
        saved_dict = json.load(json_file)
    
    assert saved_dict == expected_dict
    assert os.path.exists(json_file_path)

def test_task_func_invalid_xml():
    xml_str = "<root><child>value</chil></root>"  # Missing closing tag
    with pytest.raises(xmltodict.expat.ExpatError):
        task_func(xml_str, False, None)