python
import pytest
from src_1138 import task_func

def test_task_func():
    url = "https://www.example.com"
    output_path = "output.json"
    phone_numbers = task_func(url, output_path)
    assert isinstance(phone_numbers, list)
    assert len(phone_numbers) > 0
    assert all(isinstance(num, str) for num in phone_numbers)