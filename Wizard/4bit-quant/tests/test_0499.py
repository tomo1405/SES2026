python
import xmltodict
import json
import pytest

def task_func(s, save_json, json_file_path):
    if not s.strip():  # Check for empty or whitespace-only string
        raise ValueError("The input XML string is empty or contains only whitespace.")
    
    my_dict = xmltodict.parse(s)

    if save_json and json_file_path:
        with open(json_file_path, 'w') as json_file:
            json.dump(my_dict, json_file, indent=4)

    return my_dict

def test_task_func():
    # Test case 1: Valid XML string, save_json=True, json_file_path=None
    s = '<root><person><name>John</name><age>30</age></person></root>'
    save_json = True
    json_file_path = None
    expected_dict = {'root': {'person': {'name': 'John', 'age': '30'}}}
    assert task_func(s, save_json, json_file_path) == expected_dict

    # Test case 2: Valid XML string, save_json=False, json_file_path=None
    s = '<root><person><name>John</name><age>30</age></person></root>'
    save_json = False
    json_file_path = None
    expected_dict = {'root': {'person': {'name': 'John', 'age': '30'}}}
    assert task_func(s, save_json, json_file_path) == expected_dict

    # Test case 3: Valid XML string, save_json=True, json_file_path=valid_path
    s = '<root><person><name>John</name><age>30</age></person></root>'
    save_json = True
    json_file_path = 'test.json'
    expected_dict = {'root': {'person': {'name': 'John', 'age': '30'}}}
    assert task_func(s, save_json, json_file_path) == expected_dict

    # Test case 4: Valid XML string, save_json=False, json_file_path=valid_path
    s = '<root><person><name>John</name><age>30</age></person></root>'
    save_json = False
    json_file_path = 'test.json'
    expected_dict = {'root': {'person': {'name': 'John', 'age': '30'}}}
    assert task_func(s, save_json, json_file_path) == expected_dict

    # Test case 5: Empty XML string, save_json=True, json_file_path=None
    s = ''
    save_json = True
    json_file_path = None
    with pytest.raises(ValueError):
        task_func(s, save_json, json_file_path)

    # Test case 6: Empty XML string, save_json=False, json_file_path=None
    s = ''
    save_json = False
    json_file_path = None
    with pytest.raises(ValueError):
        task_func(s, save_json, json_file_path)

    # Test case 7: Empty XML string, save_json=True, json_file_path=valid_path
    s = ''
    save_json = True
    json_file_path = 'test.json'
    with pytest.raises(ValueError):
        task_func(s, save_json, json_file_path)

    # Test case 8: Empty XML string, save_json=False, json_file_path=valid_path
    s = ''
    save_json = False
    json_file_path = 'test.json'
    with pytest.raises(ValueError):
        task_func(s, save_json, json_file_path)

    # Test case 9: Whitespace-only XML string, save_json=True, json_file_path=None
    s = '   '
    save_json = True
    json_file_path = None
    with pytest.raises(ValueError):
        task_func(s, save_json, json_file_path)

    # Test case 10: Whitespace-only XML string, save_json=False, json_file_path=None
    s = '   '
    save_json = False
    json_file_path = None
    with pytest.raises(ValueError):
        task_func(s, save_json, json_file_path)

    # Test case 11: Whitespace-only XML string, save_json=True, json_file_path=valid_path
    s = '   '
    save_json = True
    json_file_path = 'test.json'
    with pytest.raises(ValueError):
        task_func(s, save_json, json_file_path)

    # Test case 12: Whitespace-only XML string, save_json=False, json_file_path=valid_path
    s = '   '
    save_json = False
    json_file_path = 'test.json'
    with pytest.raises(ValueError):
        task_func(s, save_json, json_file_path)