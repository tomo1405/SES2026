import pytest
from src_0190 import task_func

def test_task_func_valid_url():
    data_url = "https://jsonplaceholder.typicode.com/users"
    expected_names = ["Leanne Graham", "Ervin Howell", "Clementine Bauch", "Patricia Lebsack", "Chelsey Dietrich"]
    assert task_func(data_url) == expected_names

def test_task_func_invalid_url():
    data_url = "https://jsonplaceholder.typicode.com/invalid"
    assert task_func(data_url) == "Invalid url input"