import numpy as np
from scipy import stats
from src_0930 import task_func

def test_task_func():
    word = "hello"
    difference, entropy = task_func(word)
    assert isinstance(difference, np.ndarray)
    assert isinstance(entropy, float)
    assert len(difference) == len(word) - 1
    assert entropy >= 0 and entropy <= np.log2(len(word))

def test_task_func_empty_string():
    word = ""
    difference, entropy = task_func(word)
    assert isinstance(difference, np.ndarray)
    assert len(difference) == 0