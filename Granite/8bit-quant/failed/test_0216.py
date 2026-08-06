import pytest
from src_0216 import task_func

def test_task_func():
    url = "https://example.com/api"
    parameters = {"param1": "value1", "param2": "value2"}
    df, ax = task_func(url, parameters)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.matrix.Axes)

def test_task_func_exception():
    url = "https://example.com/api"
    parameters = {"param1": "value1", "param2": "value2"}
    with pytest.raises(Exception):
        task_func(url, parameters)