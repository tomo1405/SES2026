import pytest
from src_0353 import task_func

def test_task_func():
    text_dict = {'apple': 10, 'banana': 5, 'orange': 8}
    word_keys = ['apple', 'banana', 'orange', 'grape']
    top_k = 2

    with pytest.raises(ValueError):
        task_func(text_dict, word_keys, top_k=-1)

    ax, top_k_words = task_func(text_dict, word_keys, top_k=top_k)

    assert ax is not None
    assert isinstance(top_k_words, dict)
    assert len(top_k_words) == top_k
    assert all(word in text_dict for word in top_k_words)