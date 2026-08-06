import pytest
from src_0359 import task_func

def test_task_func():
    # Test case 1: valid JSON string and r=2
    json_list = '{"number_list": [1, 2, 3]}'
    r = 2
    expected_output = [[1, 2], [1, 3], [2, 3]]
    assert task_func(json_list, r) == expected_output

    # Test case 2: valid JSON string and r=3
    json_list = '{"number_list": [1, 2, 3]}'
    r = 3
    expected_output = [[1, 2, 3]]
    assert task_func(json_list, r) == expected_output

    # Test case 3: invalid JSON string
    json_list = '{"number_list": [1, 2, 3]'
    r = 2
    with pytest.raises(Exception):
        task_func(json_list, r)

    # Test case 4: valid JSON string and r=0
    json_list = '{"number_list": [1, 2, 3]}'
    r = 0
    expected_output = []
    assert task_func(json_list, r) == expected_output