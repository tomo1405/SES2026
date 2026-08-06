import pytest
from src_0955 import task_func

def test_task_func():
    target_words = ["hello", "world"]
    n_sentences = 5
    vocabulary = ["hello", "world", "python", "testing", "engineer"]
    expected_output = [
        "hello python engineer hello world hello python testing hello world",
        "world python engineer hello world hello python testing hello world",
        "hello python engineer hello world hello python testing hello world",
        "world python engineer hello world hello python testing hello world",
        "hello python engineer hello world hello python testing hello world"
    ]
    actual_output = task_func(target_words, n_sentences, vocabulary)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_invalid_n_sentences():
    target_words = ["hello", "world"]
    n_sentences = -1
    vocabulary = ["hello", "world", "python", "testing", "engineer"]
    with pytest.raises(ValueError) as excinfo:
        task_func(target_words, n_sentences, vocabulary)
    assert "n_sentences cannot be negative." in str(excinfo.value), "Invalid negative n_sentences error message not raised"

def test_task_func_empty_vocabulary():
    target_words = ["hello", "world"]
    n_sentences = 5
    vocabulary = []
    with pytest.raises(ValueError) as excinfo:
        task_func(target_words, n_sentences, vocabulary)
    assert "Vocabulary cannot be empty." in str(excinfo.value), "Empty vocabulary error message not raised"