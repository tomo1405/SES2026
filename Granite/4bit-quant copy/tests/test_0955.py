import random
import re
from src_0955 import task_func

def test_task_func():
    target_words = ["cat", "dog"]
    n_sentences = 3
    vocabulary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "cat", "dog"]
    expected_output = [
        "a a a a a a a a a cat",
        "b b b b b b b b b cat",
        "c c c c c c c c c cat"
    ]
    output = task_func(target_words, n_sentences, vocabulary)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_invalid_n_sentences():
    target_words = ["cat", "dog"]
    n_sentences = -1
    vocabulary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "cat", "dog"]
    with pytest.raises(ValueError) as excinfo:
        task_func(target_words, n_sentences, vocabulary)
    assert "n_sentences cannot be negative." in str(excinfo.value), "Incorrect error message"

def test_task_func_empty_vocabulary():
    target_words = ["cat", "dog"]
    n_sentences = 3
    vocabulary = []
    with pytest.raises(ValueError) as excinfo:
        task_func(target_words, n_sentences, vocabulary)
    assert "Vocabulary cannot be empty." in str(excinfo.value), "Incorrect error message"