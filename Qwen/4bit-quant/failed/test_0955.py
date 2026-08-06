import pytest
from src_0955 import task_func

def test_task_func_basic():
    target_words = ["hello", "world"]
    n_sentences = 2
    vocabulary = ["hello", "world", "foo", "bar", "baz"]
    
    result = task_func(target_words, n_sentences, vocabulary)
    assert len(result) == n_sentences
    for sentence in result:
        assert all(word.lower() in sentence for word in target_words)
        assert all(word.lower() not in sentence for word in vocabulary if word.lower() not in target_words)

def test_task_func_empty_target_words():
    target_words = []
    n_sentences = 2
    vocabulary = ["hello", "world", "foo", "bar", "baz"]
    
    result = task_func(target_words, n_sentences, vocabulary)
    assert len(result) == n_sentences
    for sentence in result:
        assert all(word.lower() not in sentence for word in vocabulary)

def test_task_func_single_sentence():
    target_words = ["test"]
    n_sentences = 1
    vocabulary = ["test", "example", "sample"]
    
    result = task_func(target_words, n_sentences, vocabulary)
    assert len(result) == n_sentences
    assert target_words[0].lower() in result[0]

def test_task_func_no_replacement():
    target_words = ["nonexistent"]
    n_sentences = 1
    vocabulary = ["test", "example", "sample"]
    
    result = task_func(target_words, n_sentences, vocabulary)
    assert len(result) == n_sentences
    assert target_words[0].lower() not in result[0]

def test_task_func_case_insensitivity():
    target_words = ["Hello"]
    n_sentences = 1
    vocabulary = ["hello", "world", "foo", "bar", "baz"]
    
    result = task_func(target_words, n_sentences, vocabulary)
    assert len(result) == n_sentences
    assert "hello" in result[0]

def test_task_func_zero_sentences():
    target_words = ["hello", "world"]
    n_sentences = 0
    vocabulary = ["hello", "world", "foo", "bar", "baz"]
    
    result = task_func(target_words, n_sentences, vocabulary)
    assert len(result) == n_sentences

def test_task_func_negative_sentences():
    target_words = ["hello", "world"]
    n_sentences = -1
    vocabulary = ["hello", "world", "foo", "bar", "baz"]
    
    with pytest.raises(ValueError, match="n_sentences cannot be negative."):
        task_func(target_words, n_sentences, vocabulary)

def test_task_func_empty_vocabulary():
    target_words = ["hello", "world"]
    n_sentences = 2
    vocabulary = []
    
    with pytest.raises(ValueError, match="Vocabulary cannot be empty."):
        task_func(target_words, n_sentences, vocabulary)