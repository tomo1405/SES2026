import pytest
from src_0175 import task_func
import pandas as pd
import numpy as np

def test_task_func_input_data_not_dataframe():
    data = "not a dataframe"
    key = "random_generated"
    min_value = 0
    max_value = 10
    with pytest.raises(ValueError):
        task_func(data, key, min_value, max_value)

def test_task_func_input_data_dataframe():
    data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    key = "random_generated"
    min_value = 0
    max_value = 10
    result = task_func(data, key, min_value, max_value)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 3)
    assert result.columns.tolist() == ["a", "b", "random_generated"]
    assert result["random_generated"].dtype == np.int64
    assert np.all(result["random_generated"] >= min_value)
    assert np.all(result["random_generated"] <= max_value)