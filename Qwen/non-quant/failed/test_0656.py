import pytest
from src_0656 import task_func
import numpy as np

@pytest.fixture
def sample_texts():
    return [
        "The quick brown fox jumps over the lazy dog",
        "Never jump over the lazy dog quickly",
        "A quick movement of the enemy will jeopardize five gunboats"
    ]

def test_task_func_with_empty_input():
    texts = []
    num_topics = 3
    topics, _ = task_func(texts, num_topics)
    assert topics == []
    assert _ is None

def test_task_func_with_no_valid_tokens_after_stopword_removal():
    texts = ["of", "the", "and"]
    num_topics = 3
    topics, _ = task_func(texts, num_topics)
    assert topics == []
    assert _ is None

def test_task_func_with_valid_input(sample_texts):
    num_topics = 2
    topics = task_func(sample_texts, num_topics)
    assert isinstance(topics, list)
    assert len(topics) == num_topics
    for topic in topics:
        assert isinstance(topic, list)
        assert all(isinstance(keyword, str) for keyword in topic)

def test_task_func_with_single_topic(sample_texts):
    num_topics = 1
    topics = task_func(sample_texts, num_topics)
    assert len(topics) == num_topics
    assert len(topics[0]) > 0

def test_task_func_with_more_topics_than_unique_words(sample_texts):
    num_topics = 10
    topics = task_func(sample_texts, num_topics)
    assert len(topics) == len(set().union(*topics))

def test_task_func_with_large_num_topics(sample_texts):
    num_topics = 100
    topics = task_func(sample_texts, num_topics)
    assert len(topics) == len(set().union(*topics))