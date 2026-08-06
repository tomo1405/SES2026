python
import re
from collections import Counter
import pytest

def task_func(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    return dict(Counter(words))

def test_task_func():
    assert task_func("The quick brown fox jumps over the lazy dog") == {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
    assert task_func("The quick brown fox jumps over the lazy dog.") == {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
    assert task_func("The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.") == {'the': 4, 'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 2, 'over': 2, 'lazy': 2, 'dog': 2}
    assert task_func("The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.") == {'the': 6, 'quick': 3, 'brown': 3, 'fox': 3, 'jumps': 3, 'over': 3, 'lazy': 3, 'dog': 3}
    assert task_func("The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.") == {'the': 8, 'quick': 4, 'brown': 4, 'fox': 4, 'jumps': 4, 'over': 4, 'lazy': 4, 'dog': 4}