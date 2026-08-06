python
import hashlib
import re

def task_func(input_str):
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str)
    hashed_str = hashlib.sha256(cleaned_str.encode()).hexdigest()

    return hashed_str

def test_task_func():
    assert task_func('Hello, World!') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    assert task_func('12345') == 'c4ca4238a0b923820dcc509a6f75849b1'
    assert task_func('abc123') == '900150983cd24fb0d6963f7d28e17f72'