import pandas as pd
import pytest
from src_0878 import task_func

def test_task_func_input_type():
    with pytest.raises(ValueError) as excinfo:
        task_func("not_a_dataframe")
    assert "data should be a DataFrame." in str(excinfo.value)

def test_task_func_input_values():
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame({"a": ["1", "2"]}))
    assert "DataFrame should only contain numeric values." in str(excinfo.value)

def test_task_func_n_components():
    data = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    with pytest.raises(ValueError) as excinfo:
        task_func(data, n_components=3)
    assert "n_components should not be greater than the number of columns in data." in str(excinfo.value)

def test_task_func_output_type():
    data = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    result = task_func(data)
    assert isinstance(result, pd.DataFrame)

def test_task_func_output_shape():
    data = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    result = task_func(data, n_components=1)
    assert result.shape == (2, 1)