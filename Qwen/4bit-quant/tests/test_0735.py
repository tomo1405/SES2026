import pytest
from src_0735 import task_func
import nltk

# Ensure the necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def test_task_func():
    # Test with a simple sentence
    content = "This is a test sentence."
    expected_output = {'DT': 1, 'PRP$': 1, 'VBZ': 1, 'JJ': 1, 'NN': 1}
    assert task_func(content) == expected_output

    # Test with a sentence that has repeated POS tags
    content = "This is a test sentence. This is another test."
    expected_output = {'DT': 2, 'PRP$': 2, 'VBZ': 2, 'JJ': 2, 'NN': 2}
    assert task_func(content) == expected_output

    # Test with a sentence that ends with punctuation
    content = "This is a test sentence!"
    expected_output = {'DT': 1, 'PRP$': 1, 'VBZ': 1, 'JJ': 1, 'NN': 1}
    assert task_func(content) == expected_output

    # Test with an empty string
    content = ""
    expected_output = {}
    assert task_func(content) == expected_output

    # Test with a single word
    content = "Single"
    expected_output = {}
    assert task_func(content) == expected_output

    # Test with a sentence that includes numbers and symbols
    content = "This is a test sentence with numbers 123 and symbols @#%."
    expected_output = {'DT': 1, 'PRP$': 1, 'VBZ': 1, 'JJ': 1, 'NN': 1}
    assert task_func(content) == expected_output