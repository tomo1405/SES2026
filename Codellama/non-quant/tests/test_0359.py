import pytest
from src_0359 import task_func

def test_task_func():
    # Test case 1: Valid JSON string
    json_list = '{"number_list": [1, 2, 3, 4, 5]}'
    r = 2
    expected_output = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    assert task_func(json_list, r) == expected_output

    # Test case 2: Invalid JSON string
    json_list = '{"number_list": [1, 2, 3, 4, 5]'
    r = 2
    with pytest.raises(Exception):
        task_func(json_list, r)

    # Test case 3: Valid JSON string with empty number_list
    json_list = '{"number_list": []}'
    r = 2
    expected_output = []
    assert task_func(json_list, r) == expected_output

    # Test case 4: Valid JSON string with number_list of length 1
    json_list = '{"number_list": [1]}'
    r = 2
    expected_output = []
    assert task_func(json_list, r) == expected_output

    # Test case 5: Valid JSON string with number_list of length 2
    json_list = '{"number_list": [1, 2]}'
    r = 2
    expected_output = [[1, 2]]
    assert task_func(json_list, r) == expected_output

    # Test case 6: Valid JSON string with number_list of length 3
    json_list = '{"number_list": [1, 2, 3]}'
    r = 2
    expected_output = [[1, 2], [1, 3], [2, 3]]
    assert task_func(json_list, r) == expected_output

    # Test case 7: Valid JSON string with number_list of length 4
    json_list = '{"number_list": [1, 2, 3, 4]}'
    r = 2
    expected_output = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert task_func(json_list, r) == expected_output

    # Test case 8: Valid JSON string with number_list of length 5
    json_list = '{"number_list": [1, 2, 3, 4, 5]}'
    r = 2
    expected_output = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    assert task_func(json_list, r) == expected_output