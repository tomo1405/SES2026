import pytest
import xmltodict
from src_0491 import task_func


def test_task_func():
    # Test case 1: Valid XML string and file path
    s = '<root><child>value</child></root>'
    file_path = 'test_file.json'
    expected_dict = {'root': {'child': 'value'}}

    assert task_func(s, file_path) == expected_dict

    # Test case 2: Invalid XML string
    s = 'invalid xml'
    file_path = 'test_file.json'

    with pytest.raises(xmltodict.ParseError):
        task_func(s, file_path)

    # Test case 3: Invalid file path
    s = '<root><child>value</child></root>'
    file_path = 'invalid_file_path.json'

    with pytest.raises(FileNotFoundError):
        task_func(s, file_path)