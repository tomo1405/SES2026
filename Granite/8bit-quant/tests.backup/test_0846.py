import pytest
from src_0846 import task_func

def test_task_func():
    text1 = "This is a sample text"
    text2 = "This is another sample text"
    cosine_similarity, levenshtein_ratio = task_func(text1, text2)
    assert 0 <= cosine_similarity <= 1
    assert 0 <= levenshtein_ratio <= 1
    text1 = "This is a very long text"
    text2 = "This is a very longer text"
    cosine_similarity, levenshtein_ratio = task_func(text1, text2)
    assert cosine_similarity < 1
    assert levenshtein_ratio < 1