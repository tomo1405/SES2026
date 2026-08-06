import pytest
from src_0359 import task_func
import json
import itertools

def test_task_func():
    json_list = '{"number_list": [1, 2, 3, 4, 5]}'
    r = 2
    expected_output = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

    actual_output = task_func(json_list, r)

    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_invalid_json():
    json_list = '{"number_list": [1, 2, 3, 4, 5'
    r = 2

    with pytest.raises(Exception) as e:
        task_func(json_list, r)

    assert str(e.value) == "Expecting property name enclosed in double quotes: line 1 column 23 (char 22)", "Exception message does not match expected message"