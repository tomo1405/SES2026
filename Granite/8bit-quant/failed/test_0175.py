import pandas as pd
import numpy as np
from src_0175 import task_func
import pytest

def test_task_func_input_type():
    data = pd.DataFrame()
    key = "random_key"
    min_value = 0
    max_value = 100
    with pytest.raises(ValueError) as exc_info:
        task_func(data, key, min_value, max_value)
    assert "Input 'data' must be a pandas DataFrame." in str(exc_info.value)

def test_task_func_output_type():
    data = pd.DataFrame()
    key = "random_key"
    min_value = 0
    max_value = 100
    output = task_func(data, key, min_value, max_value)
    assert isinstance(output, pd.DataFrame)

def test_task_func_output_content():
    data = pd.DataFrame()
    key = "random_key"
    min_value = 0
    max_value = 100
    output = task_func(data, key, min_value, max_value)
    assert key in output.columns
    assert len(output) == len(data)
    assert output[key].min() >= min_value
    assert output[key].max() <= max_value