import pytest
from src_0809 import task_func

def test_task_func():
    assert task_func("This is a test.") == 0.0
    assert task_func("This is a very positive test.") > 0.0
    assert task_func("This is a very negative test.") < 0.0
    assert task_func("This is a very long test with many words.") == 0.0
    assert task_func("This is a test with some stopwords.") == 0.0