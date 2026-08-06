import pytest
from src_1021 import task_func
import requests
import json
import chardet

def test_task_func_basic():
    url = "http://example.com/api"
    response = requests.get(url)
    content = response.content
    result = task_func(url=url)
    assert isinstance(result, dict), "The result should be a dictionary"

def test_task_func_encoding():
    url = "http://example.com/api"
    response = requests.get(url)
    content = response.content
    result = task_func(url=url)
    assert isinstance(result, dict), "The result should be a dictionary"

def test_task_func_encoding():
    url = "http://example.com/api"
    response = requests.get(url)
    content = response.content
    result = task_func(url=url)
    assert isinstance(result, dict), "The result should be a dictionary"

def test_task_func_encoding():
    url = "http://example.com/api"
    response = requests.get(url)
    content = response.content
    result = task_func(url=url)
    assert isinstance(result, dict), "The result should be a dictionary"