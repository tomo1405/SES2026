import pytest
from src_0735 import task_func
from collections import Counter

@pytest.fixture
def sample_content():
    return "This is a test sentence for testing purposes."

def test_task_func_basic(sample_content):
    result = task_func(sample_content)
    assert isinstance(result, dict)
    assert 'DT' in result  # 'This' is a DT (Determiner)
    assert 'VBZ' in result  # 'is' is a VBZ (3rd person singular present tense)
    assert 'JJ' in result  # 'a' is a JJ (Adjective)
    assert 'NN' in result  # 'test' is a NN (Noun, singular or mass)
    assert 'IN' in result  # 'for' is an IN (Preposition or subordinating conjunction)
    assert 'VBG' in result  # 'testing' is a VBG (Verb, gerund or present participle)
    assert 'NNS' in result  # 'purposes' is a NNS (Noun, plural)

def test_task_func_empty_string():
    result = task_func("")
    assert result == {}

def test_task_func_single_word():
    result = task_func("Hello")
    assert result == {}

def test_task_func_punctuation(sample_content):
    punctuated_content = sample_content + "!"
    result = task_func(punctuated_content)
    assert '!' not in result  # Punctuation should not be counted

def test_task_func_case_insensitivity():
    content = "This is a TEST sentence for TESTING purposes."
    result = task_func(content)
    assert result['NN'] == 2  # 'test' and 'TEST' should both be counted as NN

def test_task_func_large_text():
    large_text = " ".join(["word"] * 1000)
    result = task_func(large_text)
    assert result['NN'] == 999  # All words are 'word', which is an NN

def test_task_func_no_words():
    result = task_func(" ")
    assert result == {}