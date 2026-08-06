import pytest
from src_0658 import task_func

def test_task_func():
    # Test with valid inputs
    texts = ['This is a sample text', 'This is another sample text']
    stopwords = ['a', 'the']
    expected_output = Word2Vec(sentences=[[word for word in text.split() if word not in stopwords] for text in texts], vector_size=100, window=5, min_count=1, workers=4)
    assert task_func(texts, stopwords) == expected_output

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func([], [])

    with pytest.raises(ValueError):
        task_func(['This is a sample text'], [])

    with pytest.raises(ValueError):
        task_func(['This is a sample text'], ['a', 'the', 'and'])