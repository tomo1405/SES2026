import pytest
from src_0844 import task_func

def test_task_func_output_type():
    assert isinstance(task_func(1), str)

def test_task_func_sentence_count():
    n_sentences = 3
    result = task_func(n_sentences)
    assert len(result.split('.')) == n_sentences + 1  # +1 for the trailing period

def test_task_func_valid_characters():
    result = task_func(1)
    assert re.match(r'^[a-z\s.]+$', result)

def test_task_func_no_extra_spaces():
    result = task_func(1)
    assert not re.search(r'\s{2,}', result)
    assert not re.search(r'\.\s', result)

def test_task_func_period_at_end():
    result = task_func(1)
    assert result.endswith('.')

def test_task_func_randomness():
    result1 = task_func(1)
    result2 = task_func(1)
    assert result1 != result2  # Check for randomness by comparing two outputs