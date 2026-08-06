import pytest
from src_0846 import task_func

def test_task_func():
    text1 = "This is a sample text"
    text2 = "This is another sample text"
    cosine_similarity, levenshtein_ratio = task_func(text1, text2)
    assert 0 <= cosine_similarity <= 1, "Cosine similarity should be between 0 and 1"
    assert 0 <= levenshtein_ratio <= 1, "Levenshtein ratio should be between 0 and 1"