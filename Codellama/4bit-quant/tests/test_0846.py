import pytest
from src_0846 import task_func

def test_task_func():
    # Test case 1: Both texts are empty
    text1 = ''
    text2 = ''
    expected_cosine_similarity = 0.0
    expected_levenshtein_ratio = 1.0
    assert task_func(text1, text2) == (expected_cosine_similarity, expected_levenshtein_ratio)

    # Test case 2: Both texts are identical
    text1 = 'This is a test sentence.'
    text2 = 'This is a test sentence.'
    expected_cosine_similarity = 1.0
    expected_levenshtein_ratio = 1.0
    assert task_func(text1, text2) == (expected_cosine_similarity, expected_levenshtein_ratio)

    # Test case 3: Both texts are different
    text1 = 'This is a test sentence.'
    text2 = 'This is a test sentence with an added word.'
    expected_cosine_similarity = 0.95
    expected_levenshtein_ratio = 0.95
    assert task_func(text1, text2) == (expected_cosine_similarity, expected_levenshtein_ratio)

    # Test case 4: One text is empty
    text1 = 'This is a test sentence.'
    text2 = ''
    expected_cosine_similarity = 0.0
    expected_levenshtein_ratio = 0.0
    assert task_func(text1, text2) == (expected_cosine_similarity, expected_levenshtein_ratio)

    # Test case 5: One text is a substring of the other
    text1 = 'This is a test sentence.'
    text2 = 'This is a test sentence with an added word.'
    expected_cosine_similarity = 0.95
    expected_levenshtein_ratio = 0.95
    assert task_func(text1, text2) == (expected_cosine_similarity, expected_levenshtein_ratio)

    # Test case 6: Both texts are different and have different lengths
    text1 = 'This is a test sentence.'
    text2 = 'This is a test sentence with an added word. This is another sentence.'
    expected_cosine_similarity = 0.95
    expected_levenshtein_ratio = 0.95
    assert task_func(text1, text2) == (expected_cosine_similarity, expected_levenshtein_ratio)