import pytest
from src_0549 import task_func
import random
import string
import base64
import zlib

def test_task_func():
    string_length = random.randint(1, 100)
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))
    compressed_string = zlib.compress(random_string.encode('utf-8'))
    encoded_compressed_string = base64.b64encode(compressed_string)
    expected_result = encoded_compressed_string.decode('utf-8')
    actual_result = task_func(string_length)
    assert actual_result == expected_result