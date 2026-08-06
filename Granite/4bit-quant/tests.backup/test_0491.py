import pytest
from src_0491 import task_func
import xmltodict
import json

def test_task_func():
    xml_string = "<root><child>Hello, world!</child></root>"
    expected_dict = {"root": {"child": "Hello, world!"}}
    with open("test_file.json", "w") as f:
        json.dump(expected_dict, f, indent=4)

    result = task_func(xml_string, "test_file.json")
    assert result == expected_dict

def test_task_func_with_invalid_xml():
    invalid_xml = "not xml"
    with pytest.raises(Exception) as exc_info:
        task_func(invalid_xml, "test_file.json")
    assert "Invalid XML" in str(exc_info.value)