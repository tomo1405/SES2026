import pytest
from src_0844 import task_func

def test_task_func_output_type():
    result = task_func(1)
    assert isinstance(result, str), "The result should be a string."

def test_task_func_number_of_sentences():
    n_sentences = 3
    result = task_func(n_sentences)
    sentences = result.split('.')
    # Subtract one because the last split element will be an empty string
    assert len(sentences) - 1 == n_sentences, "The number of sentences should match the input."

def test_task_func_sentence_length():
    result = task_func(1)
    words = result.split()
    assert 5 <= len(words) <= 10, "Each sentence should have between 5 and 10 words."

def test_task_func_word_list():
    result = task_func(1)
    words = set(result.split())
    assert words.issubset(set(["sample", "text", "contains", "several", "words", "including"])), "All words in the result should be from the WORD_LIST."

def test_task_func_no_extra_spaces():
    result = task_func(1)
    assert '  ' not in result, "There should be no extra spaces in the result."
    assert not result.startswith(' '), "The result should not start with a space."
    assert not result.endswith(' '), "The result should not end with a space."

def test_task_func_no_unwanted_characters():
    result = task_func(1)
    assert re.match(r'^[a-z\s.]+$', result), "The result should contain only lowercase letters, spaces, and periods."

def test_task_func_single_space_between_words():
    result = task_func(1)
    assert re.match(r'^[a-z ]*\.$', result), "There should be a single space between words and no trailing spaces before periods."