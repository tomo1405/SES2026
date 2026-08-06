import pytest
from src_1101 import task_func

def test_task_func_empty_input():
    texts = ["", "   ", "\n"]
    expected_output = ([], [])
    assert task_func(texts) == expected_output

def test_task_func_no_urls():
    texts = ["This is a test.", "Another test without urls."]
    dense_matrix, feature_names = task_func(texts)
    assert isinstance(dense_matrix, list)
    assert isinstance(feature_names, list)
    assert len(dense_matrix) == len(texts)
    assert all(isinstance(row, tuple) for row in dense_matrix)
    assert all(isinstance(name, str) for name in feature_names)

def test_task_func_with_urls():
    texts = ["Check this out: http://example.com", "No url here"]
    dense_matrix, feature_names = task_func(texts)
    assert isinstance(dense_matrix, list)
    assert isinstance(feature_names, list)
    assert len(dense_matrix) == len(texts)
    assert all(isinstance(row, tuple) for row in dense_matrix)
    assert all(isinstance(name, str) for name in feature_names)
    assert "http" not in dense_matrix[0]

def test_task_func_single_word():
    texts = ["word"]
    dense_matrix, feature_names = task_func(texts)
    assert isinstance(dense_matrix, list)
    assert isinstance(feature_names, list)
    assert len(dense_matrix) == len(texts)
    assert all(isinstance(row, tuple) for row in dense_matrix)
    assert all(isinstance(name, str) for name in feature_names)
    assert len(feature_names) == 1

def test_task_func_multiple_words():
    texts = ["word1 word2", "word2 word3"]
    dense_matrix, feature_names = task_func(texts)
    assert isinstance(dense_matrix, list)
    assert isinstance(feature_names, list)
    assert len(dense_matrix) == len(texts)
    assert all(isinstance(row, tuple) for row in dense_matrix)
    assert all(isinstance(name, str) for name in feature_names)
    assert len(feature_names) >= 2