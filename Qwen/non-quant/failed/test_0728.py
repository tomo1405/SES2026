import pytest
from src_0728 import task_func
import numpy as np

@pytest.fixture
def sample_sentence():
    return "Sample sentence for testing"

def test_task_func_with_empty_string():
    result = task_func("")
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert np.all(result == 0)

def test_task_func_with_non_alphanumeric_characters():
    result = task_func("!!!@#")
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert np.all(result == 0)

def test_task_func_with_unique_words():
    result = task_func("Unique words in this sentence")
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert np.sum(result > 0) == len(set("Unique words in this sentence".split()))

def test_task_func_with_existing_words():
    result = task_func("This is a sentence")
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert result[0] > 0  # The word "This" appears in the input sentence

def test_task_func_with_repeated_words():
    result = task_func("sentence sentence")
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert result[1] > 0  # The word "sentence" appears twice in the input sentence

def test_task_func_with_case_insensitivity():
    result = task_func("another Sentence")
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert result[1] > 0  # The word "Another" should match "Another" in the sentences

def test_task_func_with_numbers():
    result = task_func("12345")
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert np.all(result == 0)  # Numbers are not considered as words

def test_task_func_with_punctuation():
    result = task_func("Hello, world!")
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)
    assert result[0] > 0  # The word "Hello" should be counted