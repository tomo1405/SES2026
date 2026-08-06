import re
import string
import random
from src_0957 import task_func

def test_task_func():
    text = "Hello, world!"
    result = task_func(text)
    assert isinstance(result, str)
    assert len(result) > 0
    assert all(c.isalnum() or c in "_-" for c in result)

def test_task_func_seed():
    text = "Hello, world!"
    seed = 42
    random.seed(seed)
    result1 = task_func(text, seed=seed)
    random.seed(seed)
    result2 = task_func(text, seed=seed)
    assert result1 == result2

def test_task_func_no_punctuation():
    text = "Hello, world!"
    result = task_func(text)
    assert all(c not in string.punctuation for c in result)

def test_task_func_replacements():
    text = "Hello, world!\tThis is a test."
    result = task_func(text)
    assert result.count(" ") == 1
    assert result.count("\t") == 1
    assert result.count("___") == 1

def test_task_func_randomness():
    text = "Hello, world!"
    result1 = task_func(text)
    result2 = task_func(text)
    assert result1 != result2