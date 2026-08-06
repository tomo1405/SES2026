import numpy as np
import pytest
from src_0728 import task_func


@pytest.fixture
def setup():
    return "Test sentence!"

def test_task_func_with_empty_string(setup):
    result = task_func("")
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)

def test_task_func_with_non_empty_string(setup):
    result = task_func(setup)
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert np.sum(result) > 0

def test_task_func_with_special_characters(setup):
    special_char_string = "Hello, world! This is a test."
    result = task_func(special_char_string)
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert np.sum(result) > 0

def test_task_func_with_numbers(setup):
    number_string = "This sentence contains numbers 123 and 456."
    result = task_func(number_string)
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert np.sum(result) > 0

def test_task_func_with_same_sentence(setup):
    same_sentence = "This is a sentence"
    result = task_func(same_sentence)
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert np.sum(result) > 0