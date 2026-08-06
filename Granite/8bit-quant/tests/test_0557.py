import numpy as np
import random
from difflib import SequenceMatcher
from src_0557 import task_func

def test_task_func():
    s = "example"
    min_length = 5
    max_length = 10
    letters = "abcdefghijklmnopqrstuvwxyz"

    generated_s, is_similar = task_func(s, min_length, max_length, letters)

    assert isinstance(generated_s, str)
    assert len(generated_s) >= min_length and len(generated_s) <= max_length
    for char in generated_s:
        assert char in letters

    assert isinstance(is_similar, bool)