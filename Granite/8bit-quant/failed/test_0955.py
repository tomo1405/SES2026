import pytest
from src_0955 import task_func

def test_task_func():
    target_words = ["cat", "dog"]
    n_sentences = 5
    vocabulary = ["cat", "dog", "pizza", "burger", "ice cream"]
    expected_output = [
        "cat pizza cat pizza cat pizza cat pizza cat pizza",
        "dog pizza dog pizza dog pizza dog pizza dog pizza",
        "cat pizza cat pizza cat pizza cat pizza cat pizza",
        "dog pizza dog pizza dog pizza dog pizza dog pizza",
        "cat pizza cat pizza cat pizza cat pizza cat pizza"
    ]
    actual_output = task_func(target_words, n_sentences, vocabulary)
    assert actual_output == expected_output

def test_task_func_invalid_n_sentences():
    target_words = ["cat", "dog"]
    n_sentences = -1
    vocabulary = ["cat", "dog", "pizza", "burger", "ice cream"]
    with pytest.raises(ValueError) as excinfo:
        task_func(target_words, n_sentences, vocabulary)
    assert "n_sentences cannot be negative." in str(excinfo.value)

def test_task_func_empty_vocabulary():
    target_words = ["cat", "dog"]
    n_sentences = 5
    vocabulary = []
    with pytest.raises(ValueError) as excinfo:
        task_func(target_words, n_sentences, vocabulary)
    assert "Vocabulary cannot be empty." in str(excinfo.value)