import pytest
from src_0809 import task_func

def test_task_func_with_no_text():
    assert task_func("") == (0.0, 0.0)

def test_task_func_with_only_stopwords():
    assert task_func("is the of and") == (0.0, 0.0)

def test_task_func_with_positive_text():
    result = task_func("I love this product")
    assert result.polarity > 0

def test_task_func_with_negative_text():
    result = task_func("I hate this product")
    assert result.polarity < 0

def test_task_func_with_neutral_text():
    result = task_func("This product is okay")
    assert result.polarity == 0.0

def test_task_func_with_repeated_words():
    result = task_func("this is is a test test")
    assert result.subjectivity == pytest.approx(0.5, abs=0.1)

def test_task_func_with_mixed_case():
    result = task_func("ThIs iS a TeSt")
    assert result.subjectivity == pytest.approx(0.5, abs=0.1)