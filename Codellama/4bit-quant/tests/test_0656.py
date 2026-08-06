import pytest
from src_0656 import task_func


def test_task_func_empty_texts():
    """Test the task function with an empty list of texts."""
    topics, _ = task_func([], 3)
    assert topics == []


def test_task_func_single_text():
    """Test the task function with a single text."""
    topics, _ = task_func(['This is a single text.'], 3)
    assert topics == [['this', 'is', 'a']]


def test_task_func_multiple_texts():
    """Test the task function with multiple texts."""
    topics, _ = task_func(['This is a single text.', 'This is another text.'], 3)
    assert topics == [['this', 'is', 'a'], ['this', 'is', 'another']]


def test_task_func_num_topics():
    """Test the task function with different numbers of topics."""
    topics, _ = task_func(['This is a single text.'], 3)
    assert len(topics) == 3
    topics, _ = task_func(['This is a single text.'], 5)
    assert len(topics) == 5


def test_task_func_stopwords():
    """Test the task function with stopwords."""
    topics, _ = task_func(['This is a single text.'], 3)
    assert 'this' not in topics[0]
    assert 'is' not in topics[0]
    assert 'a' not in topics[0]