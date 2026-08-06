import pytest
from src_0955 import task_func

def test_task_func_n_sentences_negative():
    with pytest.raises(ValueError):
        task_func(["hello", "world"], -1, ["hello", "world"])

def test_task_func_vocabulary_empty():
    with pytest.raises(ValueError):
        task_func(["hello", "world"], 1, [])

def test_task_func_valid_input():
    sentences = task_func(["hello", "world"], 1, ["hello", "world"])
    assert len(sentences) == 1
    assert sentences[0] == "hello_world"