import pytest
from src_0956 import task_func

def test_task_func_empty_text():
    with pytest.raises(ValueError):
        task_func([], "")

def test_task_func_invalid_word():
    with pytest.raises(ValueError):
        task_func(["invalid_word"], "text")

def test_task_func_valid_words():
    words = ["hello", "world"]
    text = "hello world"
    ax = task_func(words, text)
    assert ax.get_xticks() == [0, 1]
    assert ax.get_xticklabels() == ["hello", "world"]
    assert ax.get_yticks() == [1, 1]
    assert ax.get_yticklabels() == ["1", "1"]