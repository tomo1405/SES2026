import pytest
from src_0809 import task_func

def test_task_func():
    text = "This is a sample text. This is a sample text."
    expected_output = (0.0, 0.0)
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function returned incorrect output"

def test_task_func_with_positive_sentiment():
    text = "I love this movie. It's amazing!"
    expected_output = (0.5, 0.75)
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function returned incorrect output"

def test_task_func_with_negative_sentiment():
    text = "I hate this product. It's terrible!"
    expected_output = (-0.5, -0.75)
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function returned incorrect output"