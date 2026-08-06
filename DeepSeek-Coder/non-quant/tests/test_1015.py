import pytest
from src_1015 import task_func
import requests
import pandas as pd

def test_task_func_valid_url():
    url = "https://api.example.com/data"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)
    assert not df.empty, "DataFrame should not be empty"

def test_task_func_invalid_url():
    with pytest.raises(TypeError):
        task_func(12345)

def test_task_func_api_error():
    with pytest.raises(requests.HTTPError):
        task_func("invalid_url")

def test_task_func_plot_generation():
    url = "https://api.example.com/data"
    df, plot = task_func(url)
    assert plot is not None, "Plot should be generated"