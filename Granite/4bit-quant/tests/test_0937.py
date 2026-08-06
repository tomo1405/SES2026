import pytest
import numpy as np
import matplotlib.pyplot as plt
import string

from src_0937 import task_func

ALPHABET = list(string.ascii_lowercase)

def test_task_func_valid_input():
    word = "python"
    expected_output = "The word should contain only lowercase alphabetic characters."
    with pytest.raises(ValueError, match=expected_output):
        task_func(word)

def test_task_func_invalid_input():
    word = "pyth0n"
    expected_output = "The word should contain only lowercase alphabetic characters."
    with pytest.raises(ValueError, match=expected_output):
        task_func(word)

def test_task_func_valid_input_check_output():
    word = "python"
    expected_output = "Alphabetical Position of Letters in Word"
    output = task_func(word)
    assert output.get_title() == expected_output

def test_task_func_invalid_input_check_output():
    word = "pyth0n"
    expected_output = "Alphabetical Position of Letters in Word"
    output = task_func(word)
    assert output.get_title() == expected_output