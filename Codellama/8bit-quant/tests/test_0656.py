import pytest
from src_0656 import task_func


def test_task_func_empty_texts():
    """Test that task_func returns an empty list when given an empty list of texts."""
    assert task_func([], 10) == ([], None)


def test_task_func_single_text():
    """Test that task_func returns a list of topics when given a single text."""
    text = "This is a test text."
    topics = task_func([text], 10)
    assert len(topics) == 1
    assert isinstance(topics[0], list)


def test_task_func_multiple_texts():
    """Test that task_func returns a list of topics when given multiple texts."""
    texts = ["This is a test text.", "This is another test text."]
    topics = task_func(texts, 10)
    assert len(topics) == 2
    assert isinstance(topics[0], list)
    assert isinstance(topics[1], list)


def test_task_func_stopwords():
    """Test that task_func removes stopwords from the input texts."""
    text = "This is a test text."
    topics = task_func([text], 10)
    assert "is" not in topics[0]


def test_task_func_num_topics():
    """Test that task_func returns the correct number of topics."""
    text = "This is a test text."
    topics = task_func([text], 10)
    assert len(topics[0]) == 10


def test_task_func_topic_keywords():
    """Test that task_func returns the correct topic keywords."""
    text = "This is a test text."
    topics = task_func([text], 10)
    assert "test" in topics[0]
    assert "text" in topics[0]