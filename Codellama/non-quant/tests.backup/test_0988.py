import pytest
from src_0988 import task_func

def test_task_func():
    json_data = '{"key1": {"key2": [1, 2, 3, 4, 5]}}'
    data_key = "key1.key2"
    values, normalized_values, ax = task_func(json_data, data_key)

    assert values.equals(pd.Series([1, 2, 3, 4, 5], dtype=pd.Float64Dtype))
    assert normalized_values.equals(pd.Series([0.0, 0.25, 0.5, 0.75, 1.0], dtype=pd.Float64Dtype))
    assert ax.get_title() == "Comparison of Original and Normalized Data"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Value"
    assert ax.get_legend() == "Original Data"
    assert ax.get_legend() == "Normalized Data"