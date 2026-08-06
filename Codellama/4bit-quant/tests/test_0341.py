import pytest
from src_0341 import task_func

def test_task_func():
    # Test case 1: Test that the function returns a tuple with two elements
    req_data = {'name': 'John Doe', 'age': 30}
    result = task_func(req_data)
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Test case 2: Test that the first element of the tuple is a string
    assert isinstance(result[0], str)

    # Test case 3: Test that the second element of the tuple is a string
    assert isinstance(result[1], str)

    # Test case 4: Test that the first element of the tuple is a valid BLAKE3 hash
    assert len(result[0]) == 64
    assert result[0].startswith('0x')

    # Test case 5: Test that the second element of the tuple is a valid MD5 hash
    assert len(result[1]) == 32
    assert result[1].startswith('0x')

    # Test case 6: Test that the function raises a TypeError if the input is not a dictionary
    with pytest.raises(TypeError):
        task_func(123)

    # Test case 7: Test that the function raises a TypeError if the input is an empty dictionary
    with pytest.raises(TypeError):
        task_func({})