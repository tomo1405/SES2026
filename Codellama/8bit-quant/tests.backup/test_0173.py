import pytest
from src_0173 import task_func

def test_task_func_valid_json():
    json_data = '{"utc_datetime": "2023-02-13T12:00:00"}'
    assert task_func(json_data) == False

def test_task_func_invalid_json():
    json_data = '{"utc_datetime": "2023-02-13T12:00:00"'
    with pytest.raises(Exception):
        task_func(json_data)

def test_task_func_saturday():
    json_data = '{"utc_datetime": "2023-02-13T12:00:00"}'
    assert task_func(json_data) == True

def test_task_func_sunday():
    json_data = '{"utc_datetime": "2023-02-13T12:00:00"}'
    assert task_func(json_data) == True