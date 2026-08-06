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
    s = '''<root>
    <person>
        <name>John</name>
        <age>30</age>
    </person>
    <person>
        <name>Jane</name>
        <age>25</age>
    </person>
</root>'''
    file_path = 'test.json'
    my_dict = task_func(s, file_path)
    assert my_dict == {'root': {'person': [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]}}
    assert open(file_path).read() == '{\n    "root": {\n        "person": [\n            {\n                "name": "John",\n                "age": "30"\n            },\n            {\n                "name": "Jane",\n                "age": "25"\n            }\n        ]\n    }\n}\n'