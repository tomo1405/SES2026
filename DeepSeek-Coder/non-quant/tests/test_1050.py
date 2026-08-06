import pytest
from src_1050 import task_func
import pandas as pd

def test_task_func():
    # Test case 1: Basic input
    input_string = "line1\nline2\nline3"
    expected_output = pd.DataFrame({'Text': ['line1', 'line2', 'line3']})
    assert task_func(input_string=input_string) == expected_output

    # Add more test cases as needed