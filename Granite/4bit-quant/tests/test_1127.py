import re
import hashlib
import pytest

def task_func(input_str):
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str)
    hashed_str = hashlib.sha256(cleaned_str.encode()).hexdigest()

    return hashed_str

def test_task_func():
    input_str = "Hello, World!"
    expected_output = "7509e5bda0c76292ba8a0304150649b06cf667b2b51957c6191c175e83f19618"
    actual_output = task_func(input_str)
    assert actual_output == expected_output, "Task function output does not match expected output"

if __name__ == "__main__":
    pytest.main()