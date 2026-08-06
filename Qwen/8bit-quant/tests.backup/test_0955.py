import pytest
from src_0955 import task_func

def test_task_func_positive():
    target_words = ["hello", "world"]
    n_sentences = 2
    vocabulary = ["hello", "world", "foo", "bar", "baz", "qux", "quux", "corge", "grault", "garply"]
    result = task_func(target_words, n_sentences, vocabulary)
    assert len(result) == n_sentences
    for sentence in result:
        assert all(word.lower() in sentence for word in target_words)
        assert sentence.islower()

def test_task_func_negative_sentences():
    with pytest.raises(ValueError):
        task_func(["hello"], -1, ["hello", "world"])

def test_task_func_empty_vocabulary():
    with pytest.raises(ValueError):
        task_func(["hello"], 1, [])

def test_task_func_no_target_words():
    target_words = []
    n_sentences = 2
    vocabulary = ["hello", "world", "foo", "bar", "baz", "qux", "quux", "corge", "grault", "garply"]
    result = task_func(target_words, n_sentences, vocabulary)
    assert len(result) == n_sentences
    for sentence in result:
        assert all(word.lower() not in sentence for word in target_words)

def test_task_func_case_insensitivity():
    target_words = ["Hello", "WORLD"]
    n_sentences = 2
    vocabulary = ["hello", "world", "foo", "bar", "baz", "qux", "quux", "corge", "grault", "garply"]
    result = task_func(target_words, n_sentences, vocabulary)
    assert len(result) == n_sentences
    for sentence in result:
        assert "hello" in sentence
        assert "world" in sentence

def test_task_func_special_characters():
    target_words = ["hello!", "world?"]
    n_sentences = 2
    vocabulary = ["hello!", "world?", "foo", "bar", "baz", "qux", "quux", "corge", "grault", "garply"]
    result = task_func(target_words, n_sentences, vocabulary)
    assert len(result) == n_sentences
    for sentence in result:
        assert "hello!" in sentence
        assert "world?" in sentence

def test_task_func_long_vocabulary():
    target_words = ["hello"]
    n_sentences = 2
    vocabulary = [f"word_{i}" for i in range(100)]
    result = task_func(target_words, n_sentences, vocabulary)
    assert len(result) == n_sentences
    for sentence in result:
        assert "hello" in sentence