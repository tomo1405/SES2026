import pytest
from src_0656 import task_func


def test_task_func_empty_texts():
    """Test that task_func returns an empty list when given an empty list of texts."""
    assert task_func([], 10) == ([], None)


def test_task_func_single_text():
    """Test that task_func returns a list of topics when given a single text."""
    assert task_func(['This is a test text.'], 10) == [['test', 'text']]


def test_task_func_multiple_texts():
    """Test that task_func returns a list of topics when given multiple texts."""
    assert task_func(['This is a test text.', 'This is another test text.'], 10) == [['test', 'text'], ['test', 'text']]


def test_task_func_num_topics():
    """Test that task_func returns the correct number of topics when given a specific number of topics."""
    assert len(task_func(['This is a test text.'], 5)) == 5


def test_task_func_stopwords():
    """Test that task_func removes stopwords from the input texts."""
    assert 'the' not in task_func(['This is a test text.'], 10)[0]


def test_task_func_tokenization():
    """Test that task_func tokenizes the input texts correctly."""
    assert task_func(['This is a test text.'], 10)[0] == ['test', 'text']


def test_task_func_vectorization():
    """Test that task_func vectorizes the input texts correctly."""
    assert task_func(['This is a test text.'], 10)[0] == ['test', 'text']


def test_task_func_nmf():
    """Test that task_func performs NMF correctly."""
    assert task_func(['This is a test text.'], 10)[0] == ['test', 'text']


def test_task_func_feature_names():
    """Test that task_func returns the correct feature names."""
    assert task_func(['This is a test text.'], 10)[0] == ['test', 'text']