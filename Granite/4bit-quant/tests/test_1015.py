import pandas as pd
import pytest
from src_1015 import task_func


def test_task_func():
    api_url = "https://jsonplaceholder.typicode.com/posts"
    df, plot = task_func(api_url)
    assert isinstance(df, pd.DataFrame)
    assert plot is not None

def test_task_func_with_invalid_api_url():
    api_url = 123
    with pytest.raises(TypeError):
        task_func(api_url)