python
import xmltodict
import json
import pytest

def task_func(s, file_path):
    my_dict = xmltodict.parse(s)
    # Save the dictionary to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(my_dict, json_file, indent=4)

    return my_dict

def test_task_func():
    # Test case 1
    s = '<root><person><name>John</name><age>30</age></person></root>'
    file_path = 'test.json'
    expected_dict = {'root': {'person': {'name': 'John', 'age': '30'}}}
    task_func(s, file_path)
    with open(file_path, 'r') as json_file:
        actual_dict = json.load(json_file)
    assert actual_dict == expected_dict

    # Test case 2
    s = '<root><person><name>Jane</name><age>25</age></person></root>'
    file_path = 'test.json'
    expected_dict = {'root': {'person': {'name': 'Jane', 'age': '25'}}}
    task_func(s, file_path)
    with open(file_path, 'r') as json_file:
        actual_dict = json.load(json_file)
    assert actual_dict == expected_dict