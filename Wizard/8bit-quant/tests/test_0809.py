python
import pytest
from src_0809 import task_func

def test_task_func():
    text = "I love Python and I love testing!"
    expected_sentiment = 0.5
    
    assert task_func(text) == expected_sentiment