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
    with open(file_path, 'w') as f:
        json.dump({'name': 'John', 'age': 30, 'email': 'john@example.com'}, f)

    result = task_func(file_path, attribute, input_json, email_regex)
    assert result == 'John'

    os.remove(file_path)

def test_task_func_file_not_found():
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
    with open(file_path, 'w') as f:
        json.dump({'name': 'John', 'age': 30, 'email': 'john@example.com'}, f)
    os.remove(file_path)

    try:
        task_func(file_path, attribute, input_json, email_regex)
    except ValueError as e:
        assert str(e) == f'{file_path} does not exist.'

def test_task_func_missing_required_key():
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
    with open(file_path, 'w') as f:
        json.dump({'name': 'John', 'age': 30}, f)

    try:
        task_func(file_path, attribute, input_json, email_regex)
    except ValueError as e:
        assert str(e) == 'email is missing from the JSON object.'

    os.remove(file_path)

def test_task_func_invalid_type():
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
    with open(file_path, 'w') as f:
        json.dump({'name': 'John', 'age': '30', 'email': 'john@example.com'}, f)

    try:
        task_func(file_path, attribute, input_json, email_regex)
    except ValueError as e:
        assert str(e) == 'age is not of type <class \'int\'>.'

    os.remove(file_path)

def test_task_func_invalid_email():
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
    with open(file_path, 'w') as f:
        json.dump({'name': 'John', 'age': 30, 'email': 'john@example'}, f)

    try:
        task_func(file_path, attribute, input_json, email_regex)
    except ValueError as e:
        assert str(e) == 'Email is not valid.'

    os.remove(file_path)