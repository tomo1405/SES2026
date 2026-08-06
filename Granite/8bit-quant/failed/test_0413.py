import json
import base64
import unicodedata
from src_0413 import task_func

def test_task_func():
    json_file = 'test.json'
    data = {'key1': 'dmFsdWUx', 'key2': 'dmFsdWUy'}
    with open(json_file, 'w') as f:
        json.dump(data, f)

    decoded_data = task_func(json_file)

    assert decoded_data == {'key1': '~~~~~~~~~~~~', 'key2': '~~~~~~~~~~~~'}

def test_task_func_with_unicode_data():
    json_file = 'test.json'
    data = {'key1': 'a\u0394b', 'key2': 'c\u0394d'}
    with open(json_file, 'w') as f:
        json.dump(data, f)

    decoded_data = task_func(json_file)

    assert decoded_data == {'key1': 'a\u0394b', 'key2': 'c\u0394d'}