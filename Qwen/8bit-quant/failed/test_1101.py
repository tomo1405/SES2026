import pytest
from src_1101 import task_func
import numpy as np

def test_task_func_empty_input():
    texts = ["", "   ", "\t"]
    expected_output = ([], [])
    assert task_func(texts) == expected_output

def test_task_func_no_urls():
    texts = ["Hello world", "This is a test", "Another example"]
    output, feature_names = task_func(texts)
    assert len(output) == len(texts)
    assert len(feature_names) > 0

def test_task_func_with_urls():
    texts = ["Hello world http://example.com", "This is a test https://another-example.com", "Another example"]
    output, feature_names = task_func(texts)
    assert len(output) == len(texts)
    assert len(feature_names) > 0
    for text in output:
        assert "http" not in str(text)

def test_task_func_single_word():
    texts = ["Python", "Python", "Python"]
    output, feature_names = task_func(texts)
    assert len(output) == len(texts)
    assert len(feature_names) > 0
    assert feature_names[0] == "python"

def test_task_func_mixed_case():
    texts = ["Hello World", "hello world", "HELLO WORLD"]
    output, feature_names = task_func(texts)
    assert len(output) == len(texts)
    assert len(feature_names) > 0
    assert "hello" in feature_names

def test_task_func_special_characters():
    texts = ["Hello@world!", "This#is$a%test^", "Another&example*"]
    output, feature_names = task_func(texts)
    assert len(output) == len(texts)
    assert len(feature_names) > 0
    assert "hello" in feature_names
    assert "world" in feature_names
    assert "this" in feature_names
    assert "is" in feature_names
    assert "a" in feature_names
    assert "test" in feature_names
    assert "another" in feature_names
    assert "example" in feature_names

def test_task_func_large_input():
    texts = ["Python" * 1000] * 5
    output, feature_names = task_func(texts)
    assert len(output) == len(texts)
    assert len(feature_names) > 0
    assert feature_names[0] == "python"