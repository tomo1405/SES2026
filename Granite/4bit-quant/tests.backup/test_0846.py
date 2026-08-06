import re
import numpy as np
from collections import Counter
from Levenshtein import ratio
from src_0846 import task_func

def test_task_func():
    text1 = "This is a test"
    text2 = "This is a test"
    cosine_similarity, levenshtein_ratio = task_func(text1, text2)
    assert cosine_similarity == 1.0
    assert levenshtein_ratio == 1.0

def test_task_func_2():
    text1 = "This is a test"
    text2 = "This is a different test"
    cosine_similarity, levenshtein_ratio = task_func(text1, text2)
    assert 0.0 <= cosine_similarity <= 1.0
    assert 0.0 <= levenshtein_ratio <= 1.0