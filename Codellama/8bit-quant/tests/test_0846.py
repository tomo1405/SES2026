import pytest
from src_0846 import task_func

def test_task_func():
    text1 = "This is a test sentence."
    text2 = "This is another test sentence."
    expected_cosine_similarity = 0.95
    expected_levenshtein_ratio = 0.9

    cosine_similarity, levenshtein_ratio = task_func(text1, text2)

    assert cosine_similarity == expected_cosine_similarity
    assert levenshtein_ratio == expected_levenshtein_ratio