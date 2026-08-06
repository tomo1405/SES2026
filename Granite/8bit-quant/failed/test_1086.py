import pytest
from src_1086 import task_func

def test_task_func():
    text = "This is a sample text for testing."
    expected_output = ([('text', 1), ('sample', 1), ('testing.', 1), ('is', 1), ('a', 1)], <matplotlib.axes._subplots.AxesSubplot object at 0x7f8e1d1d0cf8>)
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function output does not match expected output."

if __name__ == "__main__":
    pytest.main()