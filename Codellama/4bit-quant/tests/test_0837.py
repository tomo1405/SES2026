import pytest
from src_0837 import task_func

def test_task_func():
    # Test with a valid target value
    result = task_func(target_value='332')
    assert result == {'file1.csv': 1, 'file2.csv': 2}

    # Test with a non-existent target value
    result = task_func(target_value='444')
    assert result == {}

    # Test with a simulate=True argument
    result = task_func(target_value='332', simulate=True)
    assert result == {'file1.csv': 1, 'file2.csv': 2}

    # Test with a non-existent target value and simulate=True
    result = task_func(target_value='444', simulate=True)
    assert result == {}