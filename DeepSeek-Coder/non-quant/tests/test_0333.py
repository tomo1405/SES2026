import pytest
from src_0333 import task_func
from nltk.corpus import stopwords

def test_task_func():
    # Test case 1
    text = "This is a test. This test is only a test."
    expected_result = {'test': 2, 'this': 2, 'is': 2, 'a': 2}
    assert task_func(text) == expected_result

    # Add more test cases as needed