import pytest
from src_0472 import task_func

def test_task_func_empty_list():
    result = task_func([])
    assert result.empty

def test_task_func_single_word():
    result = task_func(["Hello"])
    expected_df = pd.DataFrame({"Count": [1]}, index=["hello"])
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_multiple_words():
    result = task_func(["Hello", "world", "Hello", "WORLD"])
    expected_df = pd.DataFrame({"Count": [2, 1, 1]}, index=["hello", "world", "world"])
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_with_strip_and_lower():
    result = task_func(["  Hello  ", "WORLD  ", "hello"])
    expected_df = pd.DataFrame({"Count": [3, 1]}, index=["hello", "world"])
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_with_special_characters():
    result = task_func(["Hello!", "hello!!", "HELLO!!!"])
    expected_df = pd.DataFrame({"Count": [3]}, index=["hello"])
    pd.testing.assert_frame_equal(result, expected_df)