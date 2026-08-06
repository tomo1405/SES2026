import re
import string
import random
import pytest

def task_func(text: str, seed=None) -> str:
    if seed is not None:
        random.seed(seed)

    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)

    REPLACEMENTS = {" ": "_", "\t": "__", "\n": "___"}
    for k, v in REPLACEMENTS.items():
        text = text.replace(k, v)

    text = "".join(random.choice([k.upper(), k]) for k in text)

    return text

def test_task_func():
    # Test case 1: Test with a string without any special characters
    text = "This is a test string"
    expected_output = "THIS_IS_A_TEST_STRING"
    actual_output = task_func(text)
    assert actual_output == expected_output, "Test case 1 failed"

    # Test case 2: Test with a string containing special characters
    text = "This is a test! string with\nsome special characters."
    expected_output = "THIS_IS_A_TEST_STRING_WITH_SOME_SPECIAL_CHARACTERS"
    actual_output = task_func(text)
    assert actual_output == expected_output, "Test case 2 failed"

    # Test case 3: Test with a string containing only special characters
    text = "!@#$%^&*()_+"
    expected_output = ""
    actual_output = task_func(text)
    assert actual_output == expected_output, "Test case 3 failed"

if __name__ == "__main__":
    pytest.main()