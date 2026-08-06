import pandas as pd
from src_0988 import task_func


def test_task_func():
    json_data = '{"key1": {"key2": [1, 2, 3]}}'
    data_key = "key1.key2"
    values, normalized_values, ax = task_func(json_data, data_key)
    assert values.equals(pd.Series([1, 2, 3], dtype=pd.Float64Dtype))
    assert normalized_values.equals(pd.Series([0.5, 1, 1.5], dtype=pd.Float64Dtype))
    assert ax.get_title() == "Comparison of Original and Normalized Data"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Value"
    assert len(ax.get_legend().get_texts()) == 2
    assert ax.get_legend().get_texts()[0].get_text() == "Original Data"
    assert ax.get_legend().get_texts()[1].get_text() == "Normalized Data"