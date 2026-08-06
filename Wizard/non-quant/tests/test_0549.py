python
import random
import string
import base64
import zlib
import pytest

def task_func(string_length=100):
    # Generate a random string
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))
    
    # Compress the string
    compressed_string = zlib.compress(random_string.encode('utf-8'))
    
    # Encode the compressed string in base64
    encoded_compressed_string = base64.b64encode(compressed_string)

    return encoded_compressed_string.decode('utf-8')

def test_task_func():
    # Test with default string length
    assert len(task_func()) == 100
    
    # Test with custom string length
    assert len(task_func(50)) == 50
    
    # Test with empty string
    assert task_func(0) == ''
    
    # Test with string containing only spaces
    assert task_func(1000).isspace()