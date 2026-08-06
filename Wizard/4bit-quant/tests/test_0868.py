python
import re
import string
import pytest

def task_func(text1, text2):
    # Constants
    PUNCTUATION = string.punctuation

    cleaned_texts = []

    # Remove punctuation from each text string
    for text in [text1, text2]:
        cleaned_text = re.sub('['+re.escape(PUNCTUATION)+']', '', text)
        cleaned_texts.append(cleaned_text)

    return tuple(cleaned_texts)

def test_task_func():
    # Test case 1
    text1 = "Hello, World!"
    text2 = "Python is awesome!"
    expected_result = ("Hello World", "Python is awesome")
    assert task_func(text1, text2) == expected_result

    # Test case 2
    text1 = "I love Python!"
    text2 = "I'm learning Python."
    expected_result = ("I love Python", "I'm learning Python")
    assert task_func(text1, text2) == expected_result

    # Test case 3
    text1 = "Python is the best programming language."
    text2 = "Python is the most popular programming language."
    expected_result = ("Python is the best programming language", "Python is the most popular programming language")
    assert task_func(text1, text2) == expected_result

    # Test case 4
    text1 = "Python is a high-level programming language."
    text2 = "Python is an interpreted language."
    expected_result = ("Python is a high level programming language", "Python is an interpreted language")
    assert task_func(text1, text2) == expected_result

    # Test case 5
    text1 = "Python is a dynamically typed language."
    text2 = "Python is a statically typed language."
    expected_result = ("Python is a dynamically typed language", "Python is a statically typed language")
    assert task_func(text1, text2) == expected_result

    # Test case 6
    text1 = "Python is an interpreted language."
    text2 = "Python is a compiled language."
    expected_result = ("Python is an interpreted language", "Python is a compiled language")
    assert task_func(text1, text2) == expected_result

    # Test case 7
    text1 = "Python is a high-level programming language."
    text2 = "Python is a multi-paradigm language."
    expected_result = ("Python is a high level programming language", "Python is a multi paradigm language")
    assert task_func(text1, text2) == expected_result

    # Test case 8
    text1 = "Python is an interpreted language."
    text2 = "Python is a dynamically typed language."
    expected_result = ("Python is an interpreted language", "Python is a dynamically typed language")
    assert task_func(text1, text2) == expected_result

    # Test case 9
    text1 = "Python is a dynamically typed language."
    text2 = "Python is an interpreted language."
    expected_result = ("Python is a dynamically typed language", "Python is an interpreted language")
    assert task_func(text1, text2) == expected_result

    # Test case 10
    text1 = "Python is a high-level programming language."
    text2 = "Python is a compiled language."
    expected_result = ("Python is a high level programming language", "Python is a compiled language")
    assert task_func(text1, text2) == expected_result