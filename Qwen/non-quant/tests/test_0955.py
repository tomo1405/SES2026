import pytest
from src_0955 import task_func

def test_task_func_negative_sentences():
    with pytest.raises(ValueError):
        task_func(["word"], -1, ["word", "another_word"])

def test_task_func_empty_vocabulary():
    with pytest.raises(ValueError):
        task_func(["word"], 1, [])

def test_task_func_no_target_words():
    vocabulary = ["apple", "banana", "cherry"]
    sentences = task_func([], 3, vocabulary)
    assert len(sentences) == 3
    for sentence in sentences:
        assert all(word in vocabulary for word in sentence.split())

def test_task_func_with_target_words():
    vocabulary = ["apple", "banana", "cherry", "date"]
    target_words = ["apple", "banana"]
    sentences = task_func(target_words, 2, vocabulary)
    assert len(sentences) == 2
    for sentence in sentences:
        assert all(word in vocabulary for word in sentence.split())
        for word in target_words:
            assert word.replace(" ", "_") in sentence

def test_task_func_case_insensitivity():
    vocabulary = ["Apple", "Banana", "Cherry", "Date"]
    target_words = ["apple", "banana"]
    sentences = task_func(target_words, 2, vocabulary)
    assert len(sentences) == 2
    for sentence in sentences:
        assert all(word.lower() in sentence for word in vocabulary)
        for word in target_words:
            assert word.replace(" ", "_") in sentence

def test_task_func_randomness():
    vocabulary = ["apple", "banana", "cherry", "date"]
    target_words = ["apple", "banana"]
    sentences1 = task_func(target_words, 1, vocabulary)
    sentences2 = task_func(target_words, 1, vocabulary)
    assert sentences1 != sentences2