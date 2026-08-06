import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture
from src_0324 import task_func

def test_task_func():
    text = "John Smith [engineer] works at Google."
    word_freqs, means = task_func(text, num_gaussians=2, seed=42)
    assert isinstance(word_freqs, dict)
    assert isinstance(means, np.ndarray)
    assert len(means.shape) == 2
    assert means.shape[1] == 1
    assert len(word_freqs) == 3

def test_task_func_invalid_num_gaussians():
    text = "John Smith [engineer] works at Google."
    with pytest.raises(ValueError):
        task_func(text, num_gaussians=0, seed=42)

def test_task_func_invalid_num_gaussians_2():
    text = "John Smith [engineer] works at Google."
    with pytest.raises(Exception):
        task_func(text, num_gaussians=4, seed=42)