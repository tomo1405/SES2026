import re

from src_1101 import task_func


def test_task_func():
    texts = ["This is a test", "Another test", "A third test"]
    dense_matrix, feature_names = task_func(texts)
    assert isinstance(dense_matrix, list)
    assert isinstance(dense_matrix[0], tuple)
    assert len(dense_matrix) == len(texts)
    assert isinstance(feature_names, list)
    assert len(feature_names) > 0

def test_task_func_empty_input():
    texts = [""] * 10
    dense_matrix, feature_names = task_func(texts)
    assert dense_matrix == []
    assert feature_names == []

def test_task_func_urls():
    texts = ["This is a test", "Another test", "A third test", "http://www.example.com"]
    cleaned_texts = [re.sub('http[s]?://\S+', '', text) for text in texts]
    assert cleaned_texts != texts