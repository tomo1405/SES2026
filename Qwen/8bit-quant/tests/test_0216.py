import json

import matplotlib.pyplot as plt
import pandas as pd
import pytest
import requests
from src_0216 import task_func


def test_task_func_valid_url():
    url = "https://api.example.com/data"
    parameters = {"param1": "value1", "param2": "value2"}
    
    df, ax = task_func(url, parameters)
    
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    plt.close(ax.figure)

def test_task_func_invalid_url():
    url = "https://invalid-url.example.com/data"
    parameters = {"param1": "value1", "param2": "value2"}
    
    with pytest.raises(requests.exceptions.RequestException):
        task_func(url, parameters)

def test_task_func_no_data():
    url = "https://api.example.com/empty"
    parameters = {"param1": "value1", "param2": "value2"}
    
    with pytest.raises(json.JSONDecodeError):
        task_func(url, parameters)

def test_task_func_empty_parameters():
    url = "https://api.example.com/data"
    parameters = {}
    
    df, ax = task_func(url, parameters)
    
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    plt.close(ax.figure)