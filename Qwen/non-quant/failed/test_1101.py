import pytest
from src_1101 import task_func
import numpy as np

def test_task_func_empty_input():
    texts = ["", "", ""]
    expected_output = ([], [])
    assert task_func(texts) == expected_output

def test_task_func_no_urls():
    texts = ["Hello world", "This is a test", "Another example"]
    dense_matrix, feature_names = task_func(texts)
    assert isinstance(dense_matrix, list)
    assert isinstance(feature_names, list)
    assert len(dense_matrix) == len(texts)
    assert all(isinstance(row, tuple) for row in dense_matrix)
    assert all(isinstance(name, str) for name in feature_names)

def test_task_func_with_urls():
    texts = ["Check out this link http://example.com", "No links here", "http://another-example.org"]
    dense_matrix, feature_names = task_func(texts)
    assert isinstance(dense_matrix, list)
    assert isinstance(feature_names, list)
    assert len(dense_matrix) == len(texts)
    assert all(isinstance(row, tuple) for row in dense_matrix)
    assert all(isinstance(name, str) for name in feature_names)
    assert "http" not in " ".join(texts)

def test_task_func_single_text():
    texts = ["Single text without any urls"]
    dense_matrix, feature_names = task_func(texts)
    assert isinstance(dense_matrix, list)
    assert isinstance(feature_names, list)
    assert len(dense_matrix) == len(texts)
    assert all(isinstance(row, tuple) for row in dense_matrix)
    assert all(isinstance(name, str) for name in feature_names)

def test_task_func_identical_texts():
    texts = ["Identical text", "Identical text", "Identical text"]
    dense_matrix, feature_names = task_func(texts)
    assert isinstance(dense_matrix, list)
    assert isinstance(feature_names, list)
    assert len(dense_matrix) == len(texts)
    assert all(isinstance(row, tuple) for row in dense_matrix)
    assert all(isinstance(name, str) for name in feature_names)
    assert all(np.array_equal(dense_matrix[0], row) for row in dense_matrix)

def test_task_func_mixed_case():
    texts = ["Mixed CASE", "mixed case", "MiXeD CaSe"]
    dense_matrix, feature_names = task_func(texts)
    assert isinstance(dense_matrix, list)
    assert isinstance(feature_names, list)
    assert len(dense_matrix) == len(texts)
    assert all(isinstance(row, tuple) for row in dense_matrix)
    assert all(isinstance(name, str) for name in feature_names)