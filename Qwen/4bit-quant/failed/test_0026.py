import pytest
from src_0026 import task_func

def test_task_func():
    # Test with an empty dictionary
    assert task_func({}) == ''

    # Test with a simple dictionary
    assert task_func({'key': 'value'}) == 'eJwLSS0tTi1TLy0uUSgAABUfAA=='

    # Test with a dictionary containing numbers and strings
    assert task_func({'id': 1, 'name': 'test'}) == 'eJxLSS0tTi1TLy0uUSgyNjA='

    # Test with a nested dictionary
    assert task_func({'user': {'id': 1, 'name': 'test'}}) == 'eJxLSS0tTi1TLy0uUSgyNjA='

    # Test with a dictionary containing lists
    assert task_func({'items': [1, 2, 3]}) == 'eJwLSS0tTi1TLy0uUSgyNjA='

    # Test with a large dictionary
    large_dict = {f'key{i}': f'value{i}' for i in range(100)}
    assert isinstance(task_func(large_dict), str)

    # Test with a dictionary containing special characters
    assert task_func({'!@#': '$%^'}) == 'eJxLSS0tTi1TLy0uUSgyNjA='

    # Test with a dictionary containing None values
    assert task_func({'key': None}) == 'eJwLSS0tTi1TLy0uUSgyNjA='

    # Test with a dictionary containing True/False values
    assert task_func({'is_active': True}) == 'eJxLSS0tTi1TLy0uUSgyNjA='

    # Test with a dictionary containing float values
    assert task_func({'pi': 3.14}) == 'eJxLSS0tTi1TLy0uUSgyNjA='