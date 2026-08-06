import pytest
from src_0745 import task_func
import pandas as pd

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func(123)

def test_task_func_empty_string():
    result = task_func("")
    assert result.empty

def test_task_func_no_dollar_words():
    result = task_func("This is a test string without any dollar words.")
    assert result.empty

def test_task_func_single_dollar_word():
    result = task_func("$example $test $example")
    expected_df = pd.DataFrame({"Word": ["$example"], "Frequency": [2]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)

def test_task_func_multiple_dollar_words():
    result = task_func("$example $test $example $another $test $test")
    expected_df = pd.DataFrame({"Word": ["$test", "$example", "$another"], "Frequency": [3, 2, 1]})
    pd.testing.assert_frame_equal(result.sort_values(by="Word").reset_index(drop=True), expected_df)

def test_task_func_punctuation():
    result = task_func("$example! $test? $example $another $test $test")
    expected_df = pd.DataFrame({"Word": ["$example"], "Frequency": [2]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)

def test_task_func_whitespace():
    result = task_func("   $example   $test   $example   ")
    expected_df = pd.DataFrame({"Word": ["$example", "$test"], "Frequency": [2, 1]})
    pd.testing.assert_frame_equal(result.sort_values(by="Word").reset_index(drop=True), expected_df)