python
import pytest
from src_0658 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    texts = ['This is a test text.', 'This is another test text.']
    stopwords = ['a', 'is']
    expected_model = Word2Vec(sentences=[['test', 'text'], ['test', 'another', 'text']], vector_size=100, window=5, min_count=1, workers=4)
    actual_model = task_func(texts, stopwords)
    assert actual_model.wv.vocab == expected_model.wv.vocab
    assert actual_model.wv.vectors.shape == expected_model.wv.vectors.shape
    assert actual_model.wv.index2word == expected_model.wv.index2word

    # Test case 2: Test with empty input
    texts = []
    stopwords = None
    expected_model = Word2Vec(vector_size=100)
    actual_model = task_func(texts, stopwords)
    assert actual_model.wv.vocab == expected_model.wv.vocab
    assert actual_model.wv.vectors.shape == expected_model.wv.vectors.shape
    assert actual_model.wv.index2word == expected_model.wv.index2word

    # Test case 3: Test with invalid input (stopwords is not a list)
    texts = ['This is a test text.', 'This is another test text.']
    stopwords = 'a'
    with pytest.raises(TypeError):
        task_func(texts, stopwords)

    # Test case 4: Test with invalid input (texts is not a list)
    texts = 'This is a test text.'
    stopwords = None
    with pytest.raises(TypeError):
        task_func(texts, stopwords)