import pytest
from src_0634 import task_func

def test_task_func():
    # Test case 1: No duplicate words
    text = "This is a test sentence."
    expected_result = {"this": 1, "is": 1, "a": 1, "test": 1, "sentence": 1}
    assert task_func(text) == expected_result

    # Test case 2: Duplicate words
    text = "This is a test sentence. This is a test sentence."
    expected_result = {"this": 2, "is": 2, "a": 2, "test": 2, "sentence": 2}
    assert task_func(text) == expected_result

    # Test case 3: Stopwords
    text = "This is a test sentence. This is a test sentence."
    expected_result = {"this": 2, "is": 2, "a": 2, "test": 2, "sentence": 2}
    assert task_func(text) == expected_result

    # Test case 4: Empty input
    text = ""
    expected_result = {}
    assert task_func(text) == expected_result

    # Test case 5: Non-string input
    text = 123
    with pytest.raises(TypeError):
        task_func(text)