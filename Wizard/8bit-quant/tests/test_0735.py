python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from collections import Counter
import pytest

def task_func(content):
    words = content.split()[:-1]  # Split and remove the last word
    pos_tags = nltk.pos_tag(words)  # Tokenization is built into pos_tag for simple whitespace tokenization
    pos_counts = Counter(tag for _, tag in pos_tags)
    return dict(pos_counts)

def test_task_func():
    # Test case 1
    content = "The quick brown fox jumps over the lazy dog."
    expected_result = {'NN': 4, 'VB': 1, 'JJ': 1, 'RB': 1}
    assert task_func(content) == expected_result

    # Test case 2
    content = "The quick brown fox jumps over the lazy dog. The dog barks."
    expected_result = {'NN': 4, 'VB': 2, 'JJ': 1, 'RB': 1}
    assert task_func(content) == expected_result

    # Test case 3
    content = "The quick brown fox jumps over the lazy dog. The dog barks. The dog is lazy."
    expected_result = {'NN': 4, 'VB': 2, 'JJ': 1, 'RB': 2}
    assert task_func(content) == expected_result

    # Test case 4
    content = "The quick brown fox jumps over the lazy dog. The dog barks. The dog is lazy. The dog is quick."
    expected_result = {'NN': 4, 'VB': 3, 'JJ': 2, 'RB': 2}
    assert task_func(content) == expected_result