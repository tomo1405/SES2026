import pytest
from src_0846 import task_func

def test_task_func():
    # Test case 1: Both texts are empty
    text1 = ''
    text2 = ''
    expected_cosine_similarity = 0.0
    expected_levenshtein_ratio = 1.0
    actual_cosine_similarity, actual_levenshtein_ratio = task_func(text1, text2)
    assert actual_cosine_similarity == expected_cosine_similarity
    assert actual_levenshtein_ratio == expected_levenshtein_ratio

    # Test case 2: Texts are the same
    text1 = 'This is a test'
    text2 = 'This is a test'
    expected_cosine_similarity = 1.0
    expected_levenshtein_ratio = 1.0
    actual_cosine_similarity, actual_levenshtein_ratio = task_func(text1, text2)
    assert actual_cosine_similarity == expected_cosine_similarity
    assert actual_levenshtein_ratio == expected_levenshtein_ratio

    # Test case 3: Texts are different
    text1 = 'This is a test'
    text2 = 'This is another test'
    expected_cosine_similarity = 0.0
    expected_levenshtein_ratio = 0.5
    actual_cosine_similarity, actual_levenshtein_ratio = task_func(text1, text2)
    assert actual_cosine_similarity == expected_cosine_similarity
    assert actual_levenshtein_ratio == expected_levenshtein_ratio

    # Test case 4: Texts are very different
    text1 = 'This is a test'
    text2 = 'This is a completely different test'
    expected_cosine_similarity = 0.0
    expected_levenshtein_ratio = 0.0
    actual_cosine_similarity, actual_levenshtein_ratio = task_func(text1, text2)
    assert actual_cosine_similarity == expected_cosine_similarity
    assert actual_levenshtein_ratio == expected_levenshtein_ratio

    # Test case 5: Texts are very similar
    text1 = 'This is a test'
    text2 = 'This is a very similar test'
    expected_cosine_similarity = 0.9
    expected_levenshtein_ratio = 0.9
    actual_cosine_similarity, actual_levenshtein_ratio = task_func(text1, text2)
    assert actual_cosine_similarity == expected_cosine_similarity
    assert actual_levenshtein_ratio == expected_levenshtein_ratio