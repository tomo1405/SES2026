import pytest
from src_0807 import task_func

def test_task_func():
    # Test case 1: Test with a single word
    text = "hello"
    expected_output = Counter([('hello',)])
    actual_output = task_func(text)
    assert actual_output == expected_output

    # Test case 2: Test with multiple words
    text = "hello world"
    expected_output = Counter([('hello', 'world'), ('world',)])
    actual_output = task_func(text)
    assert actual_output == expected_output

    # Test case 3: Test with multiple words and n-grams
    text = "hello world"
    n = 3
    expected_output = Counter([('hello', 'world'), ('world',)])
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 4: Test with a long text
    text = "This is a long text with many words and n-grams."
    expected_output = Counter([('This', 'is', 'a'), ('is', 'a', 'long'), ('a', 'long', 'text'), ('long', 'text', 'with'), ('text', 'with', 'many'), ('with', 'many', 'words'), ('many', 'words', 'and'), ('words', 'and', 'n-grams'), ('and', 'n-grams', '.')])
    actual_output = task_func(text)
    assert actual_output == expected_output