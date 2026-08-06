import pytest
from src_0658 import task_func

def test_task_func():
    # Test with valid inputs
    texts = ['This is a sample text', 'This is another sample text']
    stopwords = ['is', 'a']
    model = task_func(texts, stopwords)
    assert model.vector_size == 100
    assert model.window == 5
    assert model.min_count == 1
    assert model.workers == 4
    assert len(model.wv.vocab) == 2
    assert model.wv.vocab['sample'].count == 2
    assert model.wv.vocab['text'].count == 2

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func([], None)

    with pytest.raises(ValueError):
        task_func(['This is a sample text'], ['invalid_stopword'])