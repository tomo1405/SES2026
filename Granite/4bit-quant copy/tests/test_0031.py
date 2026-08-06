import json
import os
import re
from src_0031 import task_func

def test_task_func():
    file_path = 'test.json'
    attribute = 'name'
    input_json = {
        "type": "object",
        "properties": {
            "name": {"type": str},  
            "age": {"type": int},   
            "email": {"type": str}  
        },
        "required": ["name", "age", "email"]
    }
    email_regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    data = {
        "name": "John",
        "age": 30,
        "email": "john@example.com"
    }

    with open(file_path, 'w') as f:
        json.dump(data, f)

    assert task_func(file_path, 'name', input_json, email_regex) == 'John'

    data['age'] = '30'
    with open(file_path, 'w') as f:
        json.dump(data, f)

    with open(file_path, 'r') as f:
        data = json.load(f)

    with pytest.raises(ValueError) as e:
        task_func(file_path, 'name', input_json, email_regex)
    assert str(e.value) == 'age is not of type <class \'int\'>.'

    data['age'] = 30
    data['email'] = 'johnexample.com'
    with open(file_path, 'w') as f:
        json.dump(data, f)

    with open(file_path, 'r') as f:
        data = json.load(f)

    with pytest.raises(ValueError) as e:
        task_func(file_path, 'name', input_json, email_regex)
    assert str(e.value) == 'Email is not valid.'

    os.remove(file_path)