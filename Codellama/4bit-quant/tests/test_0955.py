import pytest
from src_0955 import task_func

def test_task_func_positive_n_sentences():
    target_words = ["hello", "world"]
    n_sentences = 5
    vocabulary = ["hello", "world", "goodbye", "cruel", "world"]
    sentences = task_func(target_words, n_sentences, vocabulary)
    assert len(sentences) == n_sentences
    for sentence in sentences:
        assert sentence.lower() in vocabulary

def test_task_func_negative_n_sentences():
    target_words = ["hello", "world"]
    n_sentences = -1
    vocabulary = ["hello", "world", "goodbye", "cruel", "world"]
    with pytest.raises(ValueError):
        task_func(target_words, n_sentences, vocabulary)

def test_task_func_empty_vocabulary():
    target_words = ["hello", "world"]
    n_sentences = 5
    vocabulary = []
    with pytest.raises(ValueError):
        task_func(target_words, n_sentences, vocabulary)

def test_task_func_target_words_not_in_vocabulary():
    target_words = ["hello", "world"]
    n_sentences = 5
    vocabulary = ["goodbye", "cruel", "world"]
    sentences = task_func(target_words, n_sentences, vocabulary)
    assert len(sentences) == n_sentences
    for sentence in sentences:
        assert sentence.lower() in vocabulary

def test_task_func_target_words_in_vocabulary():
    target_words = ["hello", "world"]
    n_sentences = 5
    vocabulary = ["hello", "world", "goodbye", "cruel", "world"]
    sentences = task_func(target_words, n_sentences, vocabulary)
    assert len(sentences) == n_sentences
    for sentence in sentences:
        assert sentence.lower() in vocabulary