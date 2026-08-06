import pytest
from src_0956 import task_func
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter

def test_task_func():
    # Test case 1: Basic functionality
    mystrings = ["hello", "world"]
    text = "hello world"
    result = task_func(mystrings=mystrings, text=text)
    assert result is not None

    # Add more assertions to validate the output

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()