import pytest
from src_1095 import task_func
from nltk.tokenize import RegexpTokenizer
from collections import Counter

def test_task_func():
    text = "I have $$100 and $200 in my bank account. $100 is from my salary and the rest is from my savings account."
    expected_output = [('100', 1), ('200', 1), ('my', 1), ('in', 1), ('bank', 1)]

    tokenizer = RegexpTokenizer(r'\$\$+\w*|\$\w+')
    dollar_prefixed_words = tokenizer.tokenize(text)
    normalized_words = [word.lstrip("$") if len(word.lstrip("$")) > 0 else word for word in dollar_prefixed_words]
    word_counts = Counter(normalized_words)
    actual_output = word_counts.most_common(5)

    assert actual_output == expected_output

def test_task_func_with_empty_text():
    text = ""
    expected_output = []

    tokenizer = RegexpTokenizer(r'\$\$+\w*|\$\w+')
    dollar_prefixed_words = tokenizer.tokenize(text)
    normalized_words = [word.lstrip("$") if len(word.lstrip("$")) > 0 else word for word in dollar_prefixed_words]
    word_counts = Counter(normalized_words)
    actual_output = word_counts.most_common(5)

    assert actual_output == expected_output

def test_task_func_with_no_dollar_signs():
    text = "I have 100 and 200 in my bank account. 100 is from my salary and the rest is from my savings account."
    expected_output = [('100', 1), ('200', 1), ('my', 1), ('in', 1), ('bank', 1)]

    tokenizer = RegexpTokenizer(r'\$\$+\w*|\$\w+')
    dollar_prefixed_words = tokenizer.tokenize(text)
    normalized_words = [word.lstrip("$") if len(word.lstrip("$")) > 0 else word for word in dollar_prefixed_words]
    word_counts = Counter(normalized_words)
    actual_output = word_counts.most_common(5)

    assert actual_output == expected_output