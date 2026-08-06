python
import re
from collections import Counter
from nltk.corpus import stopwords
import pytest

def task_func(text: str) -> dict:
    words = re.findall(r'\b\w+\b', text)
    non_stopwords = [word for word in words if word.lower() not in set(stopwords.words('english'))]
    count = dict(Counter(non_stopwords))

    return count

def test_task_func():
    # Test case 1
    text = "The quick brown fox jumps over the lazy dog."
    expected_result = {'brown': 1, 'dog': 1, 'fox': 1, 'jumps': 1, 'lazy': 1, 'over': 1, 'quick': 1}
    assert task_func(text) == expected_result

    # Test case 2
    text = "The quick brown fox jumps over the lazy dog. The dog barks at the moon."
    expected_result = {'brown': 1, 'dog': 2, 'fox': 1, 'jumps': 1, 'lazy': 1, 'moon': 1, 'over': 1, 'quick': 1, 'barks': 1}
    assert task_func(text) == expected_result

    # Test case 3
    text = "The quick brown fox jumps over the lazy dog. The dog barks at the moon. The moon shines brightly."
    expected_result = {'brown': 1, 'dog': 2, 'fox': 1, 'jumps': 1, 'lazy': 1, 'moon': 2, 'over': 1, 'quick': 1, 'barks': 1, 'shines': 1}
    assert task_func(text) == expected_result

    # Test case 4
    text = "The quick brown fox jumps over the lazy dog. The dog barks at the moon. The moon shines brightly. The moon shines brightly."
    expected_result = {'brown': 1, 'dog': 2, 'fox': 1, 'jumps': 1, 'lazy': 1, 'moon': 2, 'over': 1, 'quick': 1, 'barks': 1, 'shines': 2}
    assert task_func(text) == expected_result

    # Test case 5
    text = "The quick brown fox jumps over the lazy dog. The dog barks at the moon. The moon shines brightly. The moon shines brightly. The moon shines brightly."
    expected_result = {'brown': 1, 'dog': 2, 'fox': 1, 'jumps': 1, 'lazy': 1, 'moon': 3, 'over': 1, 'quick': 1, 'barks': 1, 'shines': 3}
    assert task_func(text) == expected_result

    # Test case 6
    text = "The quick brown fox jumps over the lazy dog. The dog barks at the moon. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly."
    expected_result = {'brown': 1, 'dog': 2, 'fox': 1, 'jumps': 1, 'lazy': 1, 'moon': 4, 'over': 1, 'quick': 1, 'barks': 1, 'shines': 4}
    assert task_func(text) == expected_result

    # Test case 7
    text = "The quick brown fox jumps over the lazy dog. The dog barks at the moon. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly."
    expected_result = {'brown': 1, 'dog': 2, 'fox': 1, 'jumps': 1, 'lazy': 1, 'moon': 5, 'over': 1, 'quick': 1, 'barks': 1, 'shines': 5}
    assert task_func(text) == expected_result

    # Test case 8
    text = "The quick brown fox jumps over the lazy dog. The dog barks at the moon. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly."
    expected_result = {'brown': 1, 'dog': 2, 'fox': 1, 'jumps': 1, 'lazy': 1, 'moon': 6, 'over': 1, 'quick': 1, 'barks': 1, 'shines': 6}
    assert task_func(text) == expected_result

    # Test case 9
    text = "The quick brown fox jumps over the lazy dog. The dog barks at the moon. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly."
    expected_result = {'brown': 1, 'dog': 2, 'fox': 1, 'jumps': 1, 'lazy': 1, 'moon': 7, 'over': 1, 'quick': 1, 'barks': 1, 'shines': 7}
    assert task_func(text) == expected_result

    # Test case 10
    text = "The quick brown fox jumps over the lazy dog. The dog barks at the moon. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly. The moon shines brightly."
    expected_result = {'brown': 1, 'dog': 2, 'fox': 1, 'jumps': 1, 'lazy': 1, 'moon': 8, 'over': 1, 'quick': 1, 'barks': 1, 'shines': 8}
    assert task_func(text) == expected_result