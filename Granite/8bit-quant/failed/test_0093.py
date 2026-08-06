import pandas as pd
import pytest
from src_0093 import task_func

def test_task_func_input_data_type():
    with pytest.raises(ValueError) as excinfo:
        task_func("not_a_dataframe", 3)
    assert "Input 'data' must be a pandas DataFrame." in str(excinfo.value)

def test_task_func_n_clusters_type():
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame(), "not_an_integer")
    assert "'n_clusters' must be an integer greater than 1." in str(excinfo.value)

def test_task_func_n_clusters_value():
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame(), 1)
    assert "'n_clusters' must be an integer greater than 1." in str(excinfo.value)

def test_task_func_output_type():
    data = pd.DataFrame()
    labels, ax = task_func(data, 3)
    assert isinstance(labels, list)
    assert isinstance(ax, PathCollection)