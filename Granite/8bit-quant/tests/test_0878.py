import pandas as pd
import pytest
from src_0878 import task_func

def test_task_func_input_type():
    with pytest.raises(ValueError) as excinfo:
        task_func("not_a_dataframe")
    assert "data should be a DataFrame." in str(excinfo.value)

def test_task_func_numeric_values():
    data = pd.DataFrame({"a": [1, 2, 3], "b": ["x", "y", "z"]})
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert "DataFrame should only contain numeric values." in str(excinfo.value)

def test_task_func_n_components():
    data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    with pytest.raises(ValueError) as excinfo:
        task_func(data, n_components=3)
    assert "n_components should not be greater than the number of columns in data." in str(excinfo.value)

def test_task_func_output_type():
    data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    result = task_func(data)
    assert isinstance(result, pd.DataFrame)

def test_task_func_output_shape():
    data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    result = task_func(data, n_components=1)
    assert result.shape == (data.shape[0], 1)