import pytest
from src_1101 import task_func

def test_task_func():
    texts = ["This is a test", "Another test", "A third test"]
    dense_matrix, feature_names = task_func(texts)
    assert isinstance(dense_matrix, list)
    assert isinstance(feature_names, list)
    assert len(dense_matrix) == len(texts)
    assert len(feature_names) > 0
    for row in dense_matrix:
        assert len(row) == len(feature_names)
    for text in texts:
        assert "http" not in text