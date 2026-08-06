import matplotlib.pyplot as plt
import pytest
from src_0987 import task_func


def test_task_func_valid_json():
    json_data = '{"data": "1,2,3,4,5"}'
    key_path = ["data"]
    fig = task_func(json_data, key_path)
    assert isinstance(fig, plt.Figure)
    assert isinstance(fig.axes[0], plt.Axes)

def test_task_func_invalid_json():
    json_data = '{"data": "1,2,3,4,5"'
    key_path = ["data"]
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data, key_path)
    assert "Input malformed" in str(excinfo.value)

def test_task_func_key_error():
    json_data = '{"data": {"inner": "1,2,3,4,5"}}'
    key_path = ["wrong_key"]
    with pytest.raises(KeyError) as excinfo:
        task_func(json_data, key_path)
    assert "Key error occurred" in str(excinfo.value)

def test_task_func_empty_data_string():
    json_data = '{"data": ""}'
    key_path = ["data"]
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data, key_path)
    assert "No numeric data found or empty data string." in str(excinfo.value)

def test_task_func_non_numeric_data():
    json_data = '{"data": "a,b,c,d,e"}'
    key_path = ["data"]
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data, key_path)
    assert "Value error occurred" in str(excinfo.value)

def test_task_func_nested_keys():
    json_data = '{"outer": {"middle": {"inner": "1,2,3,4,5"}}}'
    key_path = ["outer", "middle", "inner"]
    fig = task_func(json_data, key_path)
    assert isinstance(fig, plt.Figure)
    assert isinstance(fig.axes[0], plt.Axes)