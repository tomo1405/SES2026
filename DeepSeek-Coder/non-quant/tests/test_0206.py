import pytest
from src_0206 import task_func

def test_task_func():
    # Test case 1: Normal case with multiple commands
    commands = ["ls -l", "pwd"]
    expected_output = ['output1', 'output2']  # Replace with actual outputs
    assert task_func(commands) == expected_output

    # Add more test cases as needed