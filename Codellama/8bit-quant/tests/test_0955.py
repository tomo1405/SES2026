import pytest
from src_0955 import task_func

def test_task_func_negative_n_sentences():
    with pytest.raises(ValueError):
        task_func(["hello", "world"], -1, ["hello", "world"])

def test_task_func_empty_vocabulary():
    with pytest.raises(ValueError):
        task_func(["hello", "world"], 1, [])

def test_task_func_valid_input():
    sentences = task_func(["hello", "world"], 1, ["hello", "world"])
    assert len(sentences) == 1
    assert "hello" in sentences[0]
    assert "world" in sentences[0]

def test_task_func_valid_input_with_target_words():
    sentences = task_func(["hello", "world"], 1, ["hello", "world"])
    assert len(sentences) == 1
    assert "hello" in sentences[0]
    assert "world" in sentences[0]
    assert "hello_world" not in sentences[0]

def test_task_func_valid_input_with_target_words_and_replacement():
    sentences = task_func(["hello", "world"], 1, ["hello", "world"], "hello_world")
    assert len(sentences) == 1
    assert "hello" not in sentences[0]
    assert "world" not in sentences[0]
    assert "hello_world" in sentences[0]